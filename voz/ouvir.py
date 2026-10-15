import speech_recognition as sr


class ReconhecedorVoz:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def ouvir(self):
        """Escuta e reconhece a fala do usuário"""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Ouvindo...")
            try:
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=10)
                return self.recognizer.recognize_google(audio, language="pt-PT").lower()
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                print("Não consegui entender o áudio")
                return None
            except sr.RequestError:
                print("Erro no serviço de reconhecimento")
                return None