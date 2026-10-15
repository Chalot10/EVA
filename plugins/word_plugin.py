import win32com.client as win32
import speech_recognition as sr
import os
import datetime

def ditar_no_word(parametro=None, assistente=None):
    """
    Abre um novo documento do Word e permite ditar via microfone.
    Fala 'fim' para encerrar o ditado e salvar o arquivo.
    """
    try:
        if assistente:
            assistente.falar("Abrindo Word para ditado. Diga 'fim' para encerrar.")

        # Cria nome único para o documento
        pasta = r"D:\FBN-2209\FBN_2025\Projecto_chatbot"
        if not os.path.exists(pasta):
            os.makedirs(pasta)

        nome_arquivo = f"ditado_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        # Abre o Word
        word = win32.gencache.EnsureDispatch('Word.Application')
        word.Visible = True
        doc = word.Documents.Add()
        range_obj = doc.Range(0, 0)

        # Inicializa reconhecimento de voz
        r = sr.Recognizer()
        mic = sr.Microphone()

        if assistente:
            assistente.falar("Pode começar a ditar.")

        while True:
            with mic as source:
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
            try:
                texto = r.recognize_google(audio, language="pt-PT")
                if texto.lower() == "fim":
                    break

                # Escreve no Word
                # range_obj.InsertAfter(texto + " ")
                if texto.lower() == "fim":
                    break

                elif "nova linha" in texto.lower():
                    range_obj.InsertAfter("\n")

                elif "ponto final" in texto.lower():
                    range_obj.InsertAfter(". ")

                elif "ponto continuado" in texto.lower():
                    range_obj.InsertAfter("... ")

                elif "vírgula" in texto.lower() or "virgula" in texto.lower():
                    range_obj.InsertAfter(", ")

                else:
                    range_obj.InsertAfter(texto + " ")

                range_obj.Collapse(0)  # move cursor para o final

            except sr.UnknownValueError:
                if assistente:
                    assistente.falar("Não entendi, pode repetir?")
            except sr.RequestError as e:
                if assistente:
                    assistente.falar(f"Erro no serviço de reconhecimento: {e}")

        # Salva o documento
        doc.SaveAs(caminho_arquivo)
        if assistente:
            assistente.falar(f"Ditado finalizado. Documento salvo em {caminho_arquivo}")
        print(f"Documento salvo em: {caminho_arquivo}")

    except Exception as e:
        if assistente:
            assistente.falar(f"Erro ao abrir o Word ou ditar: {e}")
        print(f"Erro no plugin word_plugin: {e}")
