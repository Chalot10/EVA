import imaplib
import smtplib
import email
import pyttsx3
import speech_recognition as sr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailPlugin:
    def __init__(self, email_user, email_pass, imap_server, smtp_server, smtp_port=587):
        self.email_user = email_user
        self.email_pass = email_pass
        self.imap_server = imap_server
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    # ---------------- Abrir caixa de entrada ----------------
    def abrir_caixa_entrada(self, num=5):
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.email_user, self.email_pass)
        mail.select("inbox")

        result, data = mail.search(None, "ALL")
        mail_ids = data[0].split()
        ultimos_emails = mail_ids[-num:]

        for msg_id in ultimos_emails:
            result, msg_data = mail.fetch(msg_id, "(RFC822)")
            raw_msg = msg_data[0][1]
            msg = email.message_from_bytes(raw_msg)
            assunto = msg["subject"]
            remetente = msg["from"]
            self.engine.say(f"Email de {remetente}, assunto: {assunto}")
            self.engine.runAndWait()

    # ---------------- Ler e-mails em voz alta ----------------
    def ler_email(self, msg_id):
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.email_user, self.email_pass)
        mail.select("inbox")
        result, msg_data = mail.fetch(msg_id, "(RFC822)")
        raw_msg = msg_data[0][1]
        msg = email.message_from_bytes(raw_msg)

        conteudo = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    conteudo = part.get_payload(decode=True).decode()
                    break
        else:
            conteudo = msg.get_payload(decode=True).decode()

        self.engine.say(conteudo)
        self.engine.runAndWait()

    # ---------------- Ditado de mensagens ----------------
    def ditar_mensagem(self):
        with sr.Microphone() as source:
            self.engine.say("Diga sua mensagem após o sinal.")
            self.engine.runAndWait()
            audio = self.recognizer.listen(source)

        try:
            mensagem = self.recognizer.recognize_google(audio, language="pt-PT")
            return mensagem
        except:
            return "Não entendi a mensagem."

    # ---------------- Enviar e-mail ----------------
    def enviar_email(self, destinatario, assunto, corpo):
        msg = MIMEMultipart()
        msg["From"] = self.email_user
        msg["To"] = destinatario
        msg["Subject"] = assunto
        msg.attach(MIMEText(corpo, "plain"))

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.email_user, self.email_pass)
        server.sendmail(self.email_user, destinatario, msg.as_string())
        server.quit()

        self.engine.say("E-mail enviado com sucesso.")
        self.engine.runAndWait()

    # ---------------- Pesquisar contatos ----------------
    def pesquisar_contato(self, contato, contatos):
        # contatos = dicionário {"nome": "email"}
        return contatos.get(contato.lower(), "Contato não encontrado.")
