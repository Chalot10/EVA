import os

def mkdir(parametro, assistente=None):
    base = r"D:\FBN-2209"  # caminho base fixo
    if not parametro:
        if assistente:
            assistente.falar("Não especificaste o nome da pasta.")
        return

    pasta = os.path.join(base, parametro.strip())  # junta caminho base + nome da pasta
    if not os.path.exists(pasta):
        os.makedirs(pasta)
        if assistente:
            assistente.falar(f"Pasta '{pasta}' criada com sucesso.")
    else:
        if assistente:
            assistente.falar(f"A pasta '{pasta}' já existe.")
