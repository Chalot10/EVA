# import speech_recognition as sr
# import pyttsx3
# import datetime
# import wikipedia
# import pywhatkit
# import webbrowser
# import json
# import time
#
#
# class Assistente:
#     def __init__(self):
#         self.audio = sr.Recognizer()
#         self.maquina = pyttsx3.init()
#         self.configurar_voz()
#         self.falando = False
#
#         # Carregar comandos do JSON
#         try:
#             with open("comandos.json", "r", encoding="utf-8") as f:
#                 self.comandos_json = json.load(f)["comandos"]
#             print("Comandos JSON carregados com sucesso!")
#         except FileNotFoundError:
#             print("Arquivo comandos.json não encontrado!")
#             self.comandos_json = []
#         except Exception as e:
#             print(f"Erro ao carregar JSON: {e}")
#             self.comandos_json = []
#
#     def configurar_voz(self):
#         """Configurar voz em português"""
#         try:
#             voices = self.maquina.getProperty('voices')
#             for voice in voices:
#                 if 'portuguese' in voice.name.lower() or 'pt' in str(voice.languages).lower():
#                     self.maquina.setProperty('voice', voice.id)
#                     break
#             self.maquina.setProperty('rate', 180)
#             self.maquina.setProperty('volume', 0.9)
#             print("Voz configurada!")
#         except Exception as e:
#             print(f"Erro ao configurar voz: {e}")
#
#     # def falar(self, texto):
#     #     """Falar texto"""
#     #     print(f"🗣️  Falando: {texto}")
#     #     try:
#     #         self.maquina.say(texto)
#     #         self.maquina.runAndWait()
#     #     except Exception as e:
#     #         print(f" Erro ao falar: {e}")
#     #
#     #
#
#     def falar(self, texto):
#         self.falando = True
#         print(f"🗣️  Falando: {texto}")
#         self.maquina.say(texto)
#         self.maquina.runAndWait()
#         self.falando = False
#
#
#     def ouvir(self):
#         """Ouvir comando de voz"""
#         try:
#             with sr.Microphone() as source:
#                 print(' Ouvindo... (Fale agora)')
#                 self.audio.adjust_for_ambient_noise(source, duration=1)
#                 voz = self.audio.listen(source, timeout=5, phrase_time_limit=5)
#                 comando = self.audio.recognize_google(voz, language='pt-PT')
#                 comando = comando.lower()
#                 print(f" Reconhecido: {comando}")
#                 return comando
#
#         except sr.UnknownValueError:
#             print(" Não entendi o áudio")
#             return None
#         except sr.RequestError as e:
#             print(f" Erro no serviço Google: {e}")
#             return None
#         except sr.WaitTimeoutError:
#             print(" Tempo esgotado")
#             return None
#         except Exception as e:
#             print(f" Erro inesperado: {e}")
#             return None
#
#     def processar_comando(self, comando):
#         """Processar comando reconhecido"""
#         if comando is None:
#             return False
#
#         print(f" Processando: {comando}")
#
#         # Verificar comandos do JSON
#         for cmd in self.comandos_json:
#             cmd_texto = cmd["comando"]
#
#             #  CORREÇÃO: Comandos com parâmetros
#             if "<" in cmd_texto and ">" in cmd_texto:
#                 # Extrair a parte base do comando (antes do <)
#                 base_cmd = cmd_texto.split("<")[0].strip()
#
#                 # Verificar se o comando falado começa com a base
#                 if comando.startswith(base_cmd):
#                     # Extrair parâmetro (tudo depois da base)
#                     parametro = comando[len(base_cmd):].strip()
#                     if parametro:  # Se tem parâmetro
#                         print(f"📋 Executando: {base_cmd} com parâmetro: {parametro}")
#                         self.executar_comando_dinamico(base_cmd, parametro)
#                         return True
#
#             # ✅ Comandos simples (sem parâmetros)
#             else:
#                 if cmd_texto.lower() in comando.lower():
#                     print(f"📋 Executando comando simples: {cmd_texto}")
#                     self.executar_comando_dinamico(cmd_texto)
#                     return True
#
#         print("❌ Nenhum comando reconhecido")
#         return False
#
#     def executar_comando_dinamico(self, comando, parametro=None):
#         """Executar comando específico"""
#         try:
#
#             if comando == "horas":
#                 hora = datetime.datetime.now().strftime('%H:%M')
#                 self.falar('Agora são' + hora)
#
#             elif comando == "data":
#                 data = datetime.datetime.now().strftime('%d/%m/%Y')
#                 self.falar('Hoje é ' + data)
#
#             elif comando == "toque" and parametro:
#                 self.falar('Tocando'+parametro)
#                 pywhatkit.playonyt(parametro)
#
#             elif comando == "abra navegador":
#                 webbrowser.open("https://www.google.com")
#
#             elif comando == "pesquise" and parametro:
#                 termo = parametro.replace(" ", "+")
#                 webbrowser.open(f"https://www.google.com/search?q={termo}")
#
#             # elif comando == "procure por" and parametro:
#             #     try:
#             #         wikipedia.set_lang("pt")
#             #         resultado = wikipedia.summary(parametro, sentences=2)
#             #         self.falar(resultado)
#             #     except wikipedia.exceptions.DisambiguationError as e:
#             #         self.falar(f"Encontrei várias opções para {parametro}. Seja mais específico.")
#             #     except wikipedia.exceptions.PageError:
#             #         self.falar(f"Não encontrei informações sobre {parametro}")
#             #     except Exception as e:
#             #         self.falar("Erro ao buscar na Wikipedia")
#
#             elif comando.strip() == "procure por":
#                 if parametro and parametro.strip():
#                     try:
#                         wikipedia.set_lang("pt")
#                         resultado = wikipedia.summary(parametro, sentences=2)
#                         print("📚 Wikipedia disse:", resultado)  # Debug
#                         for frase in resultado.split(". "):
#                             self.falar(frase)
#                     except wikipedia.exceptions.DisambiguationError:
#                         self.falar('Encontrei várias opções para' + parametro +' Seja mais específico.')
#                     except wikipedia.exceptions.PageError:
#                         self.falar('Não encontrei informações sobre' +parametro)
#                     except Exception as e:
#                         print("⚠️ Erro Wikipedia:", e)
#                         self.falar("Erro ao buscar na Wikipedia")
#                 else:
#                     self.falar("Diga o que deseja procurar.")
#
#             # elif comando.startswith("procure por"):
#             #     try:
#             #         wikipedia.set_lang("pt")
#             #         parametro = comando.replace("procure por", "").strip()
#             #         if parametro:
#             #             resultado = wikipedia.summary(parametro, sentences=2)
#             #             self.falar(resultado)
#             #         else:
#             #             self.falar("Diga o que deseja procurar.")
#             #     except wikipedia.exceptions.DisambiguationError as e:
#             #         self.falar(f"Encontrei várias opções para {parametro}. Seja mais específico.")
#             #     except wikipedia.exceptions.PageError:
#             #         self.falar(f"Não encontrei informações sobre {parametro}")
#             #     except Exception as e:
#             #         self.falar("Erro ao buscar na Wikipedia")
#
#             elif comando == "sair":
#                 self.falar("Até logo!")
#                 exit()
#
#             else:
#                 self.falar("Comando não implementado")
#         except Exception as e:
#             print(f"❌ Erro ao executar comando: {e}")
#             self.falar("Desculpe, ocorreu um erro")
#
#     def executar(self):
#         """Loop principal"""
#         self.falar("Sistema iniciado. Estou ouvindo!")
#         print("🚀 Assistente ativa! Diga um comando.")
#
#         while True:
#             try:
#                 # Só ouvir se não estiver falando
#                 if not self.falando:
#                     comando = self.ouvir()
#                     if comando:
#                         sucesso = self.processar_comando(comando)
#                         if not sucesso:
#                             self.falar("Desculpe, não reconheci esse comando")
#                     else:
#                         print("🔇 Nenhum áudio detectado")
#
#                 # Pequena pausa para não sobrecarregar
#                 time.sleep(0.1)  # Reduzi para 0.1s para ser mais responsivo
#
#             except KeyboardInterrupt:
#                 print("\n👋 Programa interrompido")
#                 break
#     # def executar(self):
#     #     """Loop principal"""
#     #     self.falar("Sistema iniciado. Estou ouvindo!")
#     #     print("🚀 Assistente ativa! Diga um comando.")
#     #
#     #     while True:
#     #         try:
#     #
#     #             comando = self.ouvir()
#     #             if comando:
#     #                 sucesso = self.processar_comando(comando)
#     #                 if not sucesso:
#     #                     self.falar("Desculpe, não reconheci esse comando")
#     #             else:
#     #                 print("🔇 Nenhum áudio detectado")
#     #
#     #             # Pequena pausa para não sobrecarregar
#     #             time.sleep(1)
#     #
#     #         except KeyboardInterrupt:
#     #             print("\n👋 Programa interrompido")
#     #             break
#
#
# # Executar a assistente
# if __name__ == "__main__":
#     assistente = Assistente()
#
#     # Teste rápido da voz
#     assistente.falar("Teste de voz. Sistema funcionando!")
#
#     assistente.executar()
#
#
# # import speech_recognition as sr
# # import pyttsx3
# # import datetime
# # import wikipedia
# # import pywhatkit
# # import json
# #
# # class Assistente:
# #     def __init__(self):
# #         self.audio = sr.Recognizer()  # objeto para reconhecer o áudio
# #         self.maquina = pyttsx3.init()  # inicializa TTS
# #
# #     def falar(self, texto):
# #         """Falar texto"""
# #         self.maquina.say(texto)
# #         self.maquina.runAndWait()
# #
# #     def ouvir(self):
# #         """Ouvir comando de voz"""
# #         try:
# #             with sr.Microphone() as source:
# #                 print('Ouvindo..')
# #                 voz = self.audio.listen(source)
# #                 comando = self.audio.recognize_google(voz, language='pt-PT')
# #                 comando = comando.lower()
# #                 print("Reconhecendo:", comando)
# #                 return comando
# #         except sr.UnknownValueError:
# #             print("Não entendi o que foi dito.")
# #             return None
# #         except sr.RequestError as e:
# #             print(f"Erro no serviço Google: {e}")
# #             return None
# #         except sr.WaitTimeoutError:
# #             print("Tempo esgotado, tente de novo.")
# #             return None
# #         except Exception as e:
# #             print(f"Erro inesperado: {e}")
# #             return None
# #
# #     def processar_comando(self, comando):
# #         """Processar comando reconhecido"""
# #         if comando is None:
# #             return
# #
# #         # Responder apenas se mencionar 'angela'
# #         if 'angela' in comando:
# #             comando = comando.replace('yuni', '')
# #             self.falar(comando)
# #
# #         # Horas
# #         if 'horas' in comando:
# #             hora = datetime.datetime.now().strftime('%H:%M')
# #             self.falar('Agora são ' + hora)
# #
# #         # Procurar na Wikipedia
# #         elif 'procure por' in comando:
# #             procurar = comando.replace('procure por', '')
# #             wikipedia.set_lang('pt')
# #             result = wikipedia.summary(procurar, sentences=1)
# #             print(result)
# #             self.falar(result)
# #             self.falar(result)
# #
# #         # Tocar música
# #         elif 'toque' in comando:
# #             musica = comando.replace('toque', '').strip()
# #             self.falar('Tocando a música ' + musica)
# #             pywhatkit.playonyt(musica)
# #
# #
# #     def executar(self):
# #         """Executar a assistente"""
# #         comando = self.ouvir()
# #         self.processar_comando(comando)
# #
# #
# # # Executar a assistente
# # if __name__ == "__main__":
# #     afn = Assistente()
# #     afn.executar()
