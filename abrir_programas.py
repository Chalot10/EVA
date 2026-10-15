import webbrowser
import subprocess
import urllib.parse
import os
import socket
import ctypes
from datetime import datetime


def parse_command(command_action, argument="", assistente=None):
    print(f"OPEN_MODULE - Comando: {command_action}, Argumento: '{argument}'")

    if command_action.startswith("web!"):
        open_link(command_action[4:], assistente)
    elif command_action.startswith("web?"):
        open_link_with_search(command_action[4:], argument, assistente)
        # if assistente:
            # assistente.falar("Pesquisando " + argument)
    elif command_action.startswith("path:"):
        open_program(command_action[5:], assistente)
        # if assistente and argument:
            # assistente.falar("Abrindo " + argument)
    elif command_action.startswith("system:"):
        executar_comando_sistema(command_action[7:], argument, assistente)
    elif command_action.startswith("media:"):
        executar_comando_midia(command_action[6:], argument, assistente)
    elif command_action == 'commands':
        reload_commands(assistente)
        # if assistente:
        #     assistente.falar("Comandos atualizados")


def open_link_with_search(link, argument="", assistente=None):
    try:
        search_url = f'{link}{urllib.parse.quote(argument)}'
        print(f"OPEN_MODULE - Abrindo pesquisa: {search_url}")
        # assistente.falar("pesquisando por " + argument)
        webbrowser.open_new(search_url)
    except Exception as e:
        print(f"Erro ao abrir pesquisa: {e}")
        if assistente:
            assistente.falar("Erro ao realizar a pesquisa")


def open_link(link, assistente=None):
    try:
        print(f"OPEN_MODULE - Abrindo link: {link}")
        # assistente.falar("abrindo " + link)
        webbrowser.open_new(link)
    except Exception as e:
        print(f"Erro ao abrir link: {e}")
        if assistente:
            assistente.falar("Erro ao abrir o link")


def open_program(path, assistente=None):
    try:
        print(f"OPEN_MODULE - Abrindo programa: {path}")
        # assistente.falar("abrindo o programa")
        subprocess.Popen([path])
    except Exception as e:
        print(f"Erro ao abrir programa {path}: {e}")
        if assistente:
            assistente.falar("Erro ao abrir programa")


def executar_comando_sistema(comando, argumento="", assistente=None):
    """Executa comandos de sistema para Windows 11"""
    try:
        if comando == "shutdown":
            # if assistente:
                # assistente.falar("Desligando computador em 10 segundos")
            subprocess.run(["shutdown", "/s", "/t", "10"])

        elif comando == "restart":
            # if assistente:
            #     assistente.falar("Reiniciando computador em 10 segundos")
            subprocess.run(["shutdown", "/r", "/t", "10"])

        elif comando == "lock":
            # if assistente:
                # assistente.falar("Bloqueando computador")
            ctypes.windll.user32.LockWorkStation()

        elif comando == "hibernate":
            # if assistente:
            #     assistente.falar("Hibernando computador")
            subprocess.run(["shutdown", "/h"])

        elif comando == "sleep":
            # if assistente:
            #     assistente.falar("Suspendo computador")
            subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"])

        elif comando == "settings":
            # if assistente:
            #     assistente.falar("Abrindo configurações")
            subprocess.run(["start", "ms-settings:"], shell=True)

        elif comando == "taskmgr":
            # if assistente:
            #     assistente.falar("Abrindo gerenciador de tarefas")
            subprocess.Popen(["taskmgr.exe"])

        elif comando == "control":
            # if assistente:
            #     assistente.falar("Abrindo painel de controle")
            subprocess.Popen(["control.exe"])

        elif comando == "diskmgmt":
            # if assistente:
            #     assistente.falar("Abrindo gerenciamento de discos")
            subprocess.Popen(["diskmgmt.msc"])

        elif comando == "devmgmt":
            # if assistente:
            #     assistente.falar("Abrindo gerenciamento de dispositivos")
            subprocess.Popen(["devmgmt.msc"])

        elif comando == "services":
            if assistente:
                assistente.falar("Abrindo serviços")
            subprocess.Popen(["services.msc"])

        elif comando == "resmon":
            # if assistente:
            #     assistente.falar("Abrindo monitor de recursos")
            subprocess.Popen(["resmon.exe"])

        elif comando == "msinfo32":
            # if assistente:
            #     assistente.falar("Abrindo informações do sistema")
            subprocess.Popen(["msinfo32.exe"])

        elif comando == "ipconfig":
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            if assistente:
                assistente.falar(f"Seu IP é {ip}")
            print(f"IP: {ip}")

        elif comando == "cls":
            os.system('cls')
            if assistente:
                assistente.falar("Tela limpa")

        elif comando == "show_time":
            hora = datetime.now().strftime("%H:%M")
            if assistente:
                assistente.falar(f"São {hora.replace(':', ' horas e ')} minutos")

        elif comando == "show_date":
            data = datetime.now().strftime("%d de %B de %Y")
            if assistente:
                assistente.falar(f"Hoje é {data}")

        elif comando == "empty_recycle_bin":
            if assistente:
                assistente.falar("Esvaziando lixeira")
            subprocess.run(["powershell", "-Command", "Clear-RecycleBin -Force"])

        elif comando == "open_downloads":
            # if assistente:
                # assistente.falar("Abrindo pasta de downloads")
            downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
            subprocess.Popen(f'explorer "{downloads_path}"', shell=True)

        elif comando == "open_documents":
            # if assistente:
            #     assistente.falar("Abrindo documentos")
            documents_path = os.path.join(os.environ['USERPROFILE'], 'Documents')
            subprocess.Popen(f'explorer "{documents_path}"', shell=True)

        elif comando == "open_pictures":
            # if assistente:
            #     assistente.falar("Abrindo imagens")
            pictures_path = os.path.join(os.environ['USERPROFILE'], 'Pictures')
            subprocess.Popen(f'explorer "{pictures_path}"', shell=True)

        elif comando == "open_videos":
            # if assistente:
            #     assistente.falar("Abrindo vídeos")
            videos_path = os.path.join(os.environ['USERPROFILE'], 'Videos')
            subprocess.Popen(f'explorer "{videos_path}"', shell=True)

        elif comando == "open_music":
            # if assistente:
            #     assistente.falar("Abrindo músicas")
            music_path = os.path.join(os.environ['USERPROFILE'], 'Music')
            subprocess.Popen(f'explorer "{music_path}"', shell=True)

        # Comandos de volume usando PowerShell
        elif comando == "volume_up":
            if assistente:
                assistente.falar("Aumentando volume")
            subprocess.run(["powershell", "-Command",
                            "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys([char]175)"])

        elif comando == "volume_down":
            if assistente:
                assistente.falar("Diminuindo volume")
            subprocess.run(["powershell", "-Command",
                            "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys([char]174)"])

        elif comando == "mute":
            if assistente:
                assistente.falar("Mutando volume")
            subprocess.run(["powershell", "-Command",
                            "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys([char]173)"])

        elif comando == "screenshot":
            if assistente:
                assistente.falar("Tirando print da tela")

            import pyautogui
            screenshot = pyautogui.screenshot()
            filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot.save(filename)
            if assistente:
                assistente.falar(f"Print salvo como {filename}")

    except Exception as e:
        print(f"Erro no comando de sistema {comando}: {e}")
        if assistente:
            assistente.falar(f"Erro ao executar comando: {str(e)}")


def executar_comando_midia(comando, argumento="", assistente=None):
    """Executa comandos de mídia"""
    try:
        if comando == "play_music":
            pasta_musicas = r"D:\FBN-2209\Music\FBN"  # Caminho da pasta
            arquivos = [os.path.join(pasta_musicas, f)
                        for f in os.listdir(pasta_musicas)
                        if f.lower().endswith(('.mp3', '.wav', '.flac'))]  # Filtra arquivos de música

            if not arquivos:
                if assistente:
                    assistente.falar("Nenhuma música encontrada na pasta")
                return

            # if assistente:
            #     assistente.falar(f"Tocando {len(arquivos)} músicas da pasta {pasta_musicas}")

            # Abre cada música usando o player padrão do Windows
            for musica in arquivos:
                subprocess.Popen([musica], shell=True)

        elif comando == "pause_music":
            # if assistente:
            #     assistente.falar("Pausando música")
            subprocess.run(
                ["powershell", "-Command", "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys(' ')"])

        elif comando == "next_track":
            # if assistente:
            #     assistente.falar("Próxima música")
            subprocess.run(
                ["powershell", "-Command", "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys({RIGHT})"])

        elif comando == "prev_track":
            # if assistente:
            #     assistente.falar("Música anterior")
            subprocess.run(
                ["powershell", "-Command", "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys({LEFT})"])

        elif comando == "search_music":
            # if assistente:
            #     assistente.falar(f"Procurando música {argumento}")
            open_link_with_search("https://www.youtube.com/results?search_query=", argumento, assistente)

        elif comando == "play_series":
            # if assistente:
            #     assistente.falar(f"Procurando série {argumento}")
            open_link_with_search("https://www.netflix.com/search?q=", argumento, assistente)

        elif comando == "play_movie":
            # if assistente:
            #     assistente.falar(f"Procurando filme {argumento}")
            open_link_with_search("https://www.netflix.com/search?q=", argumento, assistente)

        elif comando == "netflix_search":
            # if assistente:
            #     assistente.falar(f"Procurando {argumento} no Netflix")
            open_link_with_search("https://www.netflix.com/search?q=", argumento, assistente)

        elif comando == "youtube_search":
            # if assistente:
                # assistente.falar(f"Procurando {argumento} no YouTube")
            open_link_with_search("https://www.youtube.com/results?search_query=", argumento, assistente)

    except Exception as e:
        print(f"Erro no comando de mídia {comando}: {e}")
        if assistente:
            assistente.falar(f"Erro ao executar comando de mídia")


def reload_commands(assistente=None):
    if assistente:
        assistente.carregar_comandos()
