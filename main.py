# import speech_recognition as sr
# import pyttsx3
# import datetime
# import wikipedia
# import pywhatkit
# import webbrowser
# import os
# import json
#
#
# class Assistente:
#     def __init__(self):
#         self.audio = sr.Recognizer()  # objeto para reconhecer o áudio
#         self.maquina = pyttsx3.init()  # inicializa TTS
#         self.nome_assistente = "ângela"  # nome de ativação
#
#         # Configurar voz (opcional)
#         voices = self.maquina.getProperty("voices")
#         if len(voices) > 1:
#             self.maquina.setProperty("voice", voices[1].id)  # voz feminina se disponível
#         self.maquina.setProperty("rate", 180)  # velocidade da voz

#         wikipedia.set_lang("pt")
#
#     def falar(self, texto):
#         """Falar texto"""
#         print("Assistente:", texto)
#         self.maquina.say(texto)
#         self.maquina.runAndWait()
#
#     def ouvir(self):
#         """Ouvir comando de voz continuamente até detectar o nome da assistente"""
#         while True:
#             try:
#                 with sr.Microphone() as source:
#                     print('Aguardando chamar por "Angela"...')
#                     self.audio.adjust_for_ambient_noise(source)  # Ajusta para ruído ambiente
#                     voz = self.audio.listen(source)
#                     comando = self.audio.recognize_google(voz, language='pt-PT')
#                     comando = comando.lower()
#                     print("Reconhecido:", comando)
#
#                     # Verifica se o nome da assistente foi mencionado
#                     if self.nome_assistente in comando:
#                         # Remove o nome da assistente do comando e retorna
#                         comando = comando.replace(self.nome_assistente, '').strip()
#                         return comando
#
#             except sr.UnknownValueError:
#                 # Ignora quando não entende o áudio
#                 pass
#             except sr.RequestError as e:
#                 print(f"Erro no serviço Google: {e}")
#             except Exception as e:
#                 print(f"Erro inesperado: {e}")
#
#     def processar_comando(self, comando):
#         """Processar comando reconhecido"""
#         if not comando:
#             return
#
#         # Horas
#         if 'horas' in comando or 'que horas são' in comando:
#             hora = datetime.datetime.now().strftime('%H:%M')
#             self.falar('Agora são ' + hora)
#
#         # Procurar na Wikipedia
#         elif 'procure por' in comando or 'pesquise sobre' in comando:
#             procurar = comando.replace('procure por', '').replace('pesquise sobre', '').replace('na wikipedia',
#                                                                                                 '').replace(
#                 'na wikipédia', '').strip()
#             wikipedia.set_lang('pt')
#             try:
#                 result = wikipedia.summary(procurar, sentences=1)
#                 print(result)
#                 self.falar(result)
#             except wikipedia.exceptions.DisambiguationError as e:
#                 self.falar(f"Encontrei várias opções para {procurar}, por exemplo: {e.options[0]}")
#             except wikipedia.exceptions.PageError:
#                 self.falar(f"Não encontrei nada sobre {procurar} na Wikipédia")
#             except Exception as e:
#                 print("Erro Wikipedia:", e)
#                 self.falar("Ocorreu um erro ao procurar na Wikipédia")
#
#         # Tocar música
#         elif 'toque' in comando or 'toca' in comando:
#             musica = comando.replace('toque', '').replace('toca', '').strip()
#             self.falar('Tocando ' + musica)
#             pywhatkit.playonyt(musica)
#
#         # Pesquisar algo no navegador
#         elif 'pesquise por' in comando:
#             pesquise = comando.replace('pesquise por', '').strip()
#             self.falar('Pesquisando por ' + pesquise)
#             pywhatkit.search(pesquise)
#
#         # ABRIR NAVEGADOR
#         elif "abrir google" in comando:
#             self.falar("Abrindo o Google")
#             webbrowser.open("https://www.google.com")
#
#         elif 'abrir youtube' in comando:
#             self.falar("Abrindo o YouTube")
#             webbrowser.open("https://www.youtube.com")
#
#         elif 'abrir bing' in comando:
#             self.falar("Abrindo o Bing")
#             webbrowser.open("https://www.bing.com")
#
#         elif 'abrir spotify' in comando:
#             self.falar("Abrindo o Spotify")
#             webbrowser.open("https://open.spotify.com")
#
#         elif 'abrir facebook' in comando:
#             self.falar("Abrindo o Facebook")
#             webbrowser.open("https://www.facebook.com")
#
#         elif 'abrir twitter' in comando:
#             self.falar("Abrindo o Twitter")
#             webbrowser.open("https://www.twitter.com")
#
#         elif 'abrir instagram' in comando:
#             self.falar("Abrindo o Instagram")
#             webbrowser.open("https://www.instagram.com")
#
#         elif 'abrir whatsapp' in comando:
#             self.falar("Abrindo o WhatsApp Web")
#             webbrowser.open("https://web.whatsapp.com")
#
#         elif 'abrir gmail' in comando:
#             self.falar("Abrindo o Gmail")
#             webbrowser.open("https://mail.google.com")
#
#         # Abrir programas locais
#         elif 'disco local c' in comando:
#             self.falar("Abrindo o disco local C")
#             os.startfile("C:\\")
#
#         elif 'abrir calculadora' in comando:
#             self.falar("Abrindo a calculadora")
#             os.system('calc.exe')
#
#         elif 'abrir word' in comando:
#             self.falar("Abrindo o Word")
#             try:
#                 os.startfile("winword")
#             except:
#                 self.falar("Não consegui abrir o Word")
#
#         elif 'abrir excel' in comando:
#             self.falar("Abrindo o Excel")
#             try:
#                 os.startfile("excel")
#             except:
#                 self.falar("Não consegui abrir o Excel")
#
#         elif 'abrir powerpoint' in comando or 'abrir power point' in comando:
#             self.falar("Abrindo o PowerPoint")
#             try:
#                 os.startfile("powerpnt")
#             except:
#                 self.falar("Não consegui abrir o PowerPoint")
#
#         # Encerrar
#         elif 'tchau' in comando or 'adeus' in comando or 'sair' in comando:
#             self.falar("Até logo! Estarei aqui se precisar.")
#             return "sair"
#
#         # Se não reconhecer o comando
#         else:
#             self.falar("Desculpe, não entendi o comando. Pode repetir?")
#
#     def executar(self):
#         """Executar a assistente continuamente"""
#         self.falar("Olá! Eu sou a Angela. Como posso ajudar?")
#
#         while True:
#             comando = self.ouvir()
#             if comando:
#                 resultado = self.processar_comando(comando)
#                 if resultado == "sair":
#                     break
#
#
# # Executar a assistente
# if __name__ == "__main__":
#     assistente = Assistente()
#     try:
#         assistente.executar()
#     except KeyboardInterrupt:
#         print("\nPrograma interrompido pelo usuário")
#     finally:
#         assistente.maquina.stop()  # Fecha o motor de voz antes de terminar



# import speech_recognition as sr
# import pyttsx3
# import datetime
# import wikipedia
# import pywhatkit
# import webbrowser
# import os
# import json
#
# class Assistente:
#     def __init__(self):
#         self.audio = sr.Recognizer()  # objeto para reconhecer o áudio
#         self.maquina = pyttsx3.init()  # inicializa TTS
#
#         voices = self.maquina.getProperty("voices")
#         if len(voices) > 1:
#             self.maquina.setProperty("voice", voices[1].id)  # voz feminina se disponível
#         self.maquina.setProperty("rate", 180)  # velocidade da voz
#
#
#     def falar(self, texto):
#         """Falar texto"""
#         print("Assistente:", texto)
#         self.maquina.say(texto)
#         self.maquina.runAndWait()
#
#     def ouvir(self):
#         """Ouvir comando de voz"""
#         try:
#             with sr.Microphone() as source:
#                 print('Ouvindo..')
#                 voz = self.audio.listen(source)
#                 comando = self.audio.recognize_google(voz, language='pt-PT')
#                 comando = comando.lower()
#                 print("Reconhecendo:", comando)
#                 return comando
#         except sr.UnknownValueError:
#             print("Não entendi o que foi dito.")
#             return None
#         except sr.RequestError as e:
#             print(f"Erro no serviço Google: {e}")
#             return None
#         except sr.WaitTimeoutError:
#             print("Tempo esgotado, tente de novo.")
#             return None
#         except Exception as e:
#             print(f"Erro inesperado: {e}")
#             return None
#
#     def processar_comando(self, comando):
#         """Processar comando reconhecido"""
#         if comando is None:
#             return
#
#         # Responder apenas se mencionar 'angela'
#         if 'angela' in comando:
#             comando = comando.replace('angela', '')
#             self.falar(comando)
#
#         # Horas
#         if 'horas' in comando:
#             hora = datetime.datetime.now().strftime('%H:%M')
#             self.falar('Agora são ' + hora)
#
#         # Procurar na Wikipedia
#         # elif 'procure por' in comando:
#         #     procurar = comando.replace('procure por', '')
#         #     procurar = comando.replace('wikipedia', '')
#         #     procurar = comando.replace('procure na', '')
#         #     procurar = comando.replace('pesquise na', '')
#         #     wikipedia.set_lang('pt')
#         #     result = wikipedia.summary(procurar, sentences=1)
#         #     print(result)
#         #     self.falar(result)
#
#         elif 'procure por' in comando:
#             procurar = comando.replace('procure por', '').replace('na wikipedia', '').replace('na wikipédia',
#                                                                                               '').strip()
#             wikipedia.set_lang('pt')
#             try:
#                 result = wikipedia.summary(procurar, sentences=1)
#                 print(result)
#                 self.falar(result)
#             except wikipedia.exceptions.DisambiguationError as e:
#                 self.falar(f"Encontrei várias opções para {procurar}, por exemplo: {e.options[0]}")
#             except wikipedia.exceptions.PageError:
#                 self.falar(f"Não encontrei nada sobre {procurar} na Wikipédia")
#             except Exception as e:
#                 print("Erro Wikipedia:", e)
#                 self.falar("Ocorreu um erro ao procurar na Wikipédia")
#
#
#         # Tocar música
#         elif 'toque' in comando:
#             musica = comando.replace('toque', '').strip()
#             self.falar('Tocando a música ' + musica)
#             pywhatkit.playonyt(musica)
#
#             # Pesquisar algo no navagador
#         elif 'pesquise por' in comando:
#             pesquise = comando.replace('pesquise por', '')
#             self.falar('Pesquisando por' + pesquise)
#             pywhatkit.playonyt(pesquise)
#
#             # ABRIR NAVEGAFOR
#         elif "abrir google" in comando:
#             self.falar("Abrindo o Google")
#             webbrowser.open("https://www.google.com")
#
#
#         if 'youtube' in comando:
#             self.falar("Abrindo o youtube")
#             webbrowser.open("https://www.youtube.com/results?search_query=" + comando)
#             exit(0)
#
#         if 'bing' in comando:
#             self.falar("Abrindo o bing")
#             webbrowser.open("https://www.bing.com/search?q=" + comando)
#             exit(0)
#
#         if 'google' in comando:
#             webbrowser.open("https://www.google.com/search?q=" + comando)
#             exit(0)
#
#         if 'spotify' in comando:
#             webbrowser.open("https://www.spotify.com/search?q=" + comando)
#             exit(0)
#
#         if 'facebook' in comando:
#             self.falar("Abrindo o facebook")
#             webbrowser.open("https://www.facebook.com/search?q=" + comando)
#             exit(0)
#
#         if 'twitter' in comando:
#             webbrowser.open("https://www.twitter.com/search?q=" + comando)
#             exit(0)
#
#         if 'instagram' in comando:
#             webbrowser.open("https://www.instagram.com/search?q=" + comando)
#             exit(0)
#
#         if 'whatsapp' in comando:
#             webbrowser.open("https://www.whatsapp.com/search?q=" + comando)
#             exit(0)
#
#         if 'gmail' in comando:
#             webbrowser.open("https://www.gmail.com" + comando)
#             exit(0)
#
#         if 'disco local c' in comando:
#             self.falar("abrindo O disco local C")
#             os.startfile("C:\\")
#             exit(0)
#
#         if 'abrir calculadora' in comando:
#             self.falar("abrindo a calculadora")
#             loc = "C:\\windows\\system32\\calc.exe"
#             os.startfile(loc)
#             exit(0)
#
#         if 'abrir word' in comando:
#             self.falar("abrindo o word")
#             loc = r"C:\Program Files (x86)\Microsoft Office\Office14\WINWORD.EXE"
#             os.startfile(loc)
#             exit(0)
#
#         if 'abrir excel' in comando:
#             self.falar("abrindo o excel")
#             loc = r"C:\Program Files (x86)\Microsoft Office\Office14\EXCEL.EXE"
#             os.startfile(loc)
#             exit(0)
#
#         if 'abrir excel' in comando:
#             self.falar("abrindo o excel")
#             loc = r"C:\Program Files (x86)\Microsoft Office\Office14\POWERPNT.EXE"
#             os.startfile(loc)
#             exit(0)
#
#         if 'tchau' in comando:
#             self.falar("Tchau Tchau")
#             exit(0)
#
#
#     # def executar(self):
#     #     """Executar a assistente continuamente"""
#     #     while True:
#     #         comando = self.ouvir()
#     #         if comando:
#     #             self.processar_comando(comando)
#
#     # def executar(self):
#     #     while True:
#     #         comando = self.ouvir()
#     #         if comando and "angela" in comando:
#     #             self.processar_comando(comando)
#
#     def executar(self):
#         """Executar a assistente"""
#         comando = self.ouvir()
#         self.processar_comando(comando)
#
#
# if __name__ == "__main__":
#     assistente = Assistente()
#     try:
#         assistente.executar()
#     finally:
#         assistente.maquina.stop()  # Fecha o motor de voz antes de terminar


# parte de cima origi

# import win32com.client as win32
#
# # Abre o Word
# word = win32.gencache.EnsureDispatch('Word.Application')
# word.Visible = True  # True = abre visível, False = em segundo plano
#
# # Cria um novo documento
# doc = word.Documents.Add()
#
# # Insere texto
# range_obj = doc.Range(0,0)
# range_obj.InsertAfter("Olá! Este é um texto adicionado pelo assistente virtual.")
#
# # (Opcional) Salvar o documento
# doc.SaveAs(r"D:\FBN-2209\FBN_2025\Projecto_chatbot\fbn.docx")

# from docx import Document
# import os
#
# # Cria o documento
# doc = Document()
# doc.add_heading('Assistente Virtual', 0)
# doc.add_paragraph('Este é um texto que foi escrito automaticamente.')
# file_path = r"D:\FBN-2209\FBN_2025\Projecto_chatbot\afn.docx"
# doc.save(file_path)
#
# # Abre no Word
# os.startfile(file_path)



#
# from assistente import Assistente
#
# if __name__ == "__main__":
#     assistente = Assistente(comandos_file="comandos.json")
#     try:
#         assistente.executar()
#     except KeyboardInterrupt:
#         print("\nAssistente interrompido pelo usuário.")
#     finally:
#         assistente.maquina.stop()  # garante que o motor de voz seja fechado
#


# main funcional


from core.assistente import Assistente


def main():
    """Ponto de entrada principal da Yuni"""
    assistente = Assistente(
        comandos_file="comandos.json"
    )
    assistente.executar()


if __name__ == "__main__":
    main()