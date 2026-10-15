import json
import speech_recognition as sr
import pyttsx3
import importlib
import os
import io
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from gtts import gTTS
import pyglet
import pygame
from pydub import AudioSegment



class Assistente:
    def __init__(self, comandos_file="comandos.json"):
        self.recognizer = sr.Recognizer()
        self.maquina = pyttsx3.init()
        voices = self.maquina.getProperty("voices")
        if len(voices) > 1:
            self.maquina.setProperty("voice", voices[1].id)
        self.maquina.setProperty("rate", 180)
        self.comandos_file = comandos_file
        self.carregar_comandos()
        # self.fila_fala = queue.Queue()
        # self.executando_fala = False
        # self.carregar_comandos()


    def carregar_comandos(self):
        with open(self.comandos_file, "r", encoding="utf-8") as f:
            self.comandos = json.load(f)["comandos"]


    def falar(self, texto):
        print("Assistente:", texto)
        try:
            # Gerar áudio diretamente na memória
            tts = gTTS(text=texto, lang='pt', slow=False)
            audio_buffer = io.BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)

            # Inicializar pygame mixer se não estiver inicializado
            if not pygame.mixer.get_init():
                pygame.mixer.init()

            # Carregar e reproduzir áudio da memória
            audio_buffer.seek(0)
            pygame.mixer.music.load(audio_buffer)
            pygame.mixer.music.play()

            # Esperar até terminar a reprodução
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(f"Erro ao falar: {e}")

    def ouvir(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Ouvindo...")
            try:
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=10)
                return self.recognizer.recognize_google(audio, language="pt-PT").lower()
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                self.falar("Não consegui entender o áudio")
                return None
            except sr.RequestError:
                self.falar("Erro no serviço de reconhecimento")
                return None

    def processar_comando(self, comando):
        if not comando:
            return

        comando = comando.lower().strip()

        for categoria in self.comandos:
            for key, lista_comandos in categoria.items():
                for item in lista_comandos:
                    for frase, detalhe in item.items():
                        if isinstance(detalhe, dict):
                            func_path = detalhe.get("acao")
                            resposta = detalhe.get("resposta", "")

                            # comando com wildcard (*)
                            if "*" in frase:
                                base = frase.replace("*", "").strip()
                                if comando.startswith(base):
                                    parametro = comando[len(base):].strip()
                                    self.executar_plugin(func_path, parametro)
                                    if resposta:
                                        self.falar(resposta.replace("{param}", parametro))
                                    return

                            # comando exato
                            elif frase == comando:
                                self.executar_plugin(func_path)
                                if resposta:
                                    self.falar(resposta)
                                return

        self.falar("Desculpe, não entendi o comando.")

    def executar_plugin(self, func_path, parametro=None):
        if parametro is None:
            parametro = ""

        # Importa e usa o open_module para comandos internos
        if func_path.startswith(('web!', 'web?', 'path:', 'commands', 'system:', 'media:')):
            from abrir_programas import parse_command
            parse_command(func_path, parametro, self)

        # Comandos de alarme (quando é um dicionário)
        elif isinstance(func_path, dict):
            from colocar_alarme import parse_command as parse_alarm_command
            from colocar_alarme import extract_argument_with_time

            # Extrai argumento e tempo do comando
            argument, when = extract_argument_with_time(
                parametro,
                list(self.comandos[0]['alarme'][0].keys())[0],  # Pega o primeiro comando de alarme
                func_path['time_indicator']
            )

            parse_alarm_command(func_path, argument, when, self)

        else:
            # Comando de plugin externo
            try:
                parts = func_path.split(".")
                if len(parts) < 2:
                    raise ValueError(f"Caminho inválido: {func_path}")

                module_name = ".".join(parts[:-1])  # tudo menos o último
                func_name = parts[-1]  # último é a função

                plugin = importlib.import_module(module_name)
                func = getattr(plugin, func_name)

                if parametro:
                    func(parametro, self)
                else:
                    func(self)

            except ImportError:
                self.falar(f"Módulo {module_name} não encontrado")
            except AttributeError:
                self.falar(f"Função {func_name} não existe no módulo {module_name}")
            except Exception as e:
                self.falar(f"Erro ao executar comando: {str(e)}")


    def executar(self):
        self.falar("Olá! Sou seu assistente.")
        self.falar("Em que posso ajudar?")

        while True:
            try:
                comando = self.ouvir()
                if comando and comando.strip():
                    self.processar_comando(comando)
            except KeyboardInterrupt:
                self.falar("Encerrando assistente. Até logo!")
                break
            except Exception as e:
                print(f"Erro inesperado: {e}")
                continue
