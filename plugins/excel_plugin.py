import win32com.client as win32
import os
import datetime
import speech_recognition as sr

def ditar_no_excel(parametro=None, assistente=None):
    """
    Abre o Excel e permite ditar valores para células.
    Fala 'fim' para encerrar o ditado e salvar o arquivo.
    """
    try:
        if assistente:
            assistente.falar("Abrindo Excel para ditado. Diga 'fim' para encerrar.")

        # Pasta e nome do arquivo
        pasta = r"D:\FBN-2209\FBN_2025\Projecto_chatbot"
        if not os.path.exists(pasta):
            os.makedirs(pasta)

        nome_arquivo = f"planilha_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        # Abre o Excel
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True
        wb = excel.Workbooks.Add()
        ws = wb.Worksheets(1)

        # Inicializa reconhecimento de voz
        r = sr.Recognizer()
        mic = sr.Microphone()

        if assistente:
            assistente.falar("Pode começar a ditar. Diga célula e valor. Exemplo: célula A1 valor 50.")

        while True:
            with mic as source:
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)

            try:
                texto = r.recognize_google(audio, language="pt-PT")
                if texto.lower() == "fim":
                    break

                # Interpreta comandos do tipo: "célula A1 valor 20"
                if "célula" in texto.lower() and "valor" in texto.lower():
                    partes = texto.lower().split("valor")
                    celula = partes[0].replace("célula", "").strip().upper()
                    valor = partes[1].strip()
                    ws.Range(celula).Value = valor
                    if assistente:
                        assistente.falar(f"Escrevi {valor} na célula {celula}")
                else:
                    if assistente:
                        assistente.falar("Formato inválido. Diga: célula A1 valor 20.")

            except sr.UnknownValueError:
                if assistente:
                    assistente.falar("Não entendi, pode repetir?")
            except sr.RequestError as e:
                if assistente:
                    assistente.falar(f"Erro no serviço de reconhecimento: {e}")

        # Salva planilha
        wb.SaveAs(caminho_arquivo)
        if assistente:
            assistente.falar(f"Planilha salva em {caminho_arquivo}")
        print(f"Planilha salva em: {caminho_arquivo}")

    except Exception as e:
        if assistente:
            assistente.falar(f"Erro ao abrir ou editar Excel: {e}")
        print(f"Erro no plugin excel_plugin: {e}")
