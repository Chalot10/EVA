import webbrowser
import subprocess
import urllib.parse


def parse_command(command_action, argument="", assistente=None):
    print(f"OPEN_MODULE - Comando: {command_action}, Argumento: '{argument}'")

    if command_action.startswith("web!"):
        open_link(command_action[4:], assistente)
    elif command_action.startswith("web?"):
        open_link_with_search(command_action[4:], argument, assistente)
        if assistente:
            assistente.falar("Pesquisando " + argument)
    elif command_action.startswith("path:"):
        open_program(command_action[5:], assistente)
        if assistente and argument:
            assistente.falar("Abrindo " + argument)
    elif command_action == 'commands':
        reload_commands(assistente)
        if assistente:
            assistente.falar("Comandos atualizados")


def open_link_with_search(link, argument="", assistente=None):
    try:
        search_url = f'{link}/search?q={urllib.parse.quote(argument)}'
        print(f"OPEN_MODULE - Abrindo pesquisa: {search_url}")
        webbrowser.open_new(search_url)
    except Exception as e:
        print(f"Erro ao abrir pesquisa: {e}")
        if assistente:
            assistente.falar("Erro ao realizar a pesquisa")


def open_link(link, assistente=None):
    try:
        print(f"OPEN_MODULE - Abrindo link: {link}")
        webbrowser.open_new(link)
    except Exception as e:
        print(f"Erro ao abrir link: {e}")
        if assistente:
            assistente.falar("Erro ao abrir o link")


def open_program(path, assistente=None):
    try:
        print(f"OPEN_MODULE - Abrindo programa: {path}")
        subprocess.Popen([path])
    except Exception as e:
        print(f"Erro ao abrir programa {path}: {e}")
        if assistente:
            assistente.falar("Erro ao abrir programa")


def reload_commands(assistente=None):
    if assistente:
        assistente.carregar_comandos()



# import webbrowser
# import subprocess
# from assistente import Assistente
#
# assistente = Assistente()
#
# def parse_command(command_action, argument=""):
#     if command_action[0:4] == "web!":
#         open_link(command_action[5:])
#     elif command_action[0:4] == "web?":
#         open_link_with_search(command_action[5:], argument)
#         assistente.falar("Pesquisando " + argument)
#     elif command_action[0:4] == "path":
#         open_program(command_action[5:])
#         assistente.falar("Abrindo " + argument)
#     elif command_action == 'commands':
#         reload_commands()
#         assistente.falar("Comandos atualizados")
#
# def open_link_with_search(link, argument=""):
#     webbrowser.get('windows-default').open_new(f'{link}/search?q={argument}')
#
# def open_link(link):
#     webbrowser.get('windows-default').open_new(link)
#
# def open_program(path):
#     try:
#         subprocess.Popen([path])
#     except Exception as e:
#         assistente.falar(f"Erro ao abrir programa: {str(e)}")
#
# def reload_commands():
#     assistente.read_commands_file()


# import os
# from assistente import Assistente
#
# assistente = Assistente()
#
#
#
# def abrir_word():
#     try:
#         assistente.falar("Abrindo a word..")
#         os.startfile(r"C:\Program Files (x86)\Microsoft Office\Office14\WINWORD.EXE")
#     except:
#         assistente.falar("Não consegui abrir o Word")
#
# def abrir_excel():
#     try:
#         assistente.falar("Abrindo o excel...")
#         os.startfile(r"C:\Program Files (x86)\Microsoft Office\Office14\EXCEL.EXE")
#     except:
#         assistente.falar("Não consegui abrir o Excel")
#
# def abrir_powerpoint():
#     try:
#         assistente.falar("Abrindo o powerpoint...")
#         os.startfile(r"C:\Program Files (x86)\Microsoft Office\Office14\POWERPNT.EXE")
#     except:
#         assistente.falar("Nao consegui abrir o powerpoint")
#
#
# def abrir_calculadora():
#     try:
#         assistente.falar("Abrindo a calculadora...")
#         os.startfile(r"C:\\windows\\system32\\calc.exe")
#     except:
#         assistente.falar("Nao consegui abrir a Calculadora")
#
#
# def abrir_whatsapp():
#     try:
#         assistente.falar("Abrindo o whatsapp...")
#         os.startfile(r"C:\\windows\\system32\\calc.exe")
#     except:
#         assistente.falar("Nao consegui abrir o whatsapp")
#
#
# def abrir_notepad():
#     try:
#         assistente.falar("Abrindo o notepad...")
#         os.startfile(r"C:\\windows\\system32\\calc.exe")
#     except:
#         assistente.falar("Nao consegui abrir o notepad")
#
#
#
# # def abrir_calculadora():
# #     try:
# #         os.startfile(r"C:\\windows\\system32\\calc.exe")
# #     except:
# #         print("Nao consegui abrir o Calculadora")
# #
# #
# # def abrir_calculadora():
# #     try:
# #         os.startfile(r"C:\\windows\\system32\\calc.exe")
# #     except:
# #         print("Nao consegui abrir o Calculadora")
# #
#
