import os
import tempfile
from gtts import gTTS
import playsound3
import pyttsx3


class SintetizadorVoz:
    def __init__(self):
        # Inicializa o pyttsx3 como fallback
        self.maquina = pyttsx3.init()

        voices = self.maquina.getProperty("voices")

        if len(voices) > 1:
            self.maquina.setProperty("voice", voices[1].id)

        self.maquina.setProperty("rate", 180)

    def falar(self, texto):
        """Fala o texto usando gTTS"""

        print("Assistente:", texto)

        ficheiro = None

        try:
            # Criar ficheiro temporário MP3
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp3"
            ) as temp:
                ficheiro = temp.name

            # Gerar voz
            tts = gTTS(
                text=texto,
                lang="pt",
                slow=False
            )

            tts.save(ficheiro)

            # Reproduzir
            playsound3.playsound(ficheiro)

        except Exception as e:

            print(f"Erro no gTTS: {e}")

            # Fallback para pyttsx3
            try:
                self.maquina.say(texto)
                self.maquina.runAndWait()

            except Exception as erro:
                print(f"Erro crítico na síntese de voz: {erro}")

        finally:

            # Apagar ficheiro temporário
            if ficheiro and os.path.exists(ficheiro):

                try:
                    os.remove(ficheiro)
                except:
                    pass


# import io
# import os
# import pygame
# from gtts import gTTS
# import pyttsx3
#
#
# class SintetizadorVoz:
#     def __init__(self):
#         # Inicializa o pyttsx3 como fallback
#         self.maquina = pyttsx3.init()
#         voices = self.maquina.getProperty("voices")
#         if len(voices) > 1:
#             self.maquina.setProperty("voice", voices[1].id)
#         self.maquina.setProperty("rate", 180)
#
#         # Configura o pygame mixer
#         if not pygame.mixer.get_init():
#             pygame.mixer.init()
#
#     def falar(self, texto):
#         """Fala o texto usando gTTS"""
#         print("Assistente:", texto)
#         try:
#             # Gerar áudio com gTTS
#             tts = gTTS(text=texto, lang='pt', slow=False)
#             audio_buffer = io.BytesIO()
#             tts.write_to_fp(audio_buffer)
#             audio_buffer.seek(0)
#
#             # Reproduzir áudio
#             audio_buffer.seek(0)
#             pygame.mixer.music.load(audio_buffer)
#             pygame.mixer.music.play()
#
#             # Esperar terminar
#             while pygame.mixer.music.get_busy():
#                 pygame.time.Clock().tick(10)
#
#         except Exception as e:
#             print(f"Erro ao falar: {e}")
#             # Fallback para pyttsx3
#             try:
#                 self.maquina.say(texto)
#                 self.maquina.runAndWait()
#             except:
#                 print("Erro crítico na síntese de voz")