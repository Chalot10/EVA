import os
import shutil

def organizar_desktop(assistente=None):
    """
    Move todas as pastas do Desktop do usuário para a pasta FBN
    """
    try:
        # Caminho do Desktop do usuário
        desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        # Pasta destino
        destino = r"D:\FBN-2209\AFN"

        if not os.path.exists(destino):
            os.makedirs(destino)
            if assistente:
                assistente.falar(f"Pasta de destino criada: {destino}")

        # Lista todas as pastas no Desktop
        for item in os.listdir(desktop):
            item_path = os.path.join(desktop, item)
            if os.path.isdir(item_path):  # verifica se é pasta
                shutil.move(item_path, destino)
                # if assistente:
                #     assistente.falar(f"Pasta '{item}' movida para '{destino}'")

        if assistente:
            assistente.falar("Todas as pastas do Desktop foram movidas com sucesso.")

    except Exception as e:
        if assistente:
            assistente.falar(f"Erro ao organizar Desktop: {e}")
        print(f"Erro no plugin organizar_desktop: {e}")
