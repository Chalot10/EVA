import os
import shutil


def executar(parametro, assistente):
    """Organiza ficheiros numa pasta por tipo"""
    pasta = parametro if parametro else os.path.expanduser("~/Downloads")

    categorias = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documentos': ['.pdf', '.docx', '.doc', '.txt', '.xlsx'],
        'Vídeos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Músicas': ['.mp3', '.wav', '.flac'],
        'Comprimidos': ['.zip', '.rar', '.7z'],
        'Instaladores': ['.exe', '.msi'],
    }

    movidos = 0
    for ficheiro in os.listdir(pasta):
        caminho = os.path.join(pasta, ficheiro)
        if os.path.isfile(caminho):
            ext = os.path.splitext(ficheiro)[1].lower()
            for categoria, extensoes in categorias.items():
                if ext in extensoes:
                    destino = os.path.join(pasta, categoria)
                    os.makedirs(destino, exist_ok=True)
                    shutil.move(caminho, os.path.join(destino, ficheiro))
                    movidos += 1
                    break

    assistente.falar(f"Organizados {movidos} ficheiros em {pasta}")