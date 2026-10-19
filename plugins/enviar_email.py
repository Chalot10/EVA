import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()


def executar(parametro, assistente):
    """Envia email com anexo"""
    # Formato esperado: "email@exemplo.com | assunto | caminho/anexo.pdf"
    partes = parametro.split("|")

    if len(partes) < 2:
        assistente.falar("Formato: email | assunto | caminho do anexo")
        return

    destinatario = partes[0].strip()
    assunto = partes[1].strip()
    anexo = partes[2].strip() if len(partes) > 2 else None

    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = os.getenv("EMAIL_USER")
    msg['To'] = destinatario
    msg.set_content("Email enviado pela EVA.")

    if anexo and os.path.exists(anexo):
        with open(anexo, 'rb') as f:
            msg.add_attachment(
                f.read(),
                maintype='application',
                subtype='octet-stream',
                filename=os.path.basename(anexo)
            )

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD"))
            smtp.send_message(msg)
        assistente.falar(f"Email enviado para {destinatario}")
    except Exception as e:
        assistente.falar(f"Erro ao enviar email: {e}")