import os
import re

def executar_comando(entrada):
    # Detecta criação de pasta
    padrao = r"(criar pasta|nova pasta|fazer pasta) (.*)"
    match = re.match(padrao, entrada.lower())
    if match:
        nome_pasta = match.group(2).strip()
        try:
            os.makedirs(nome_pasta, exist_ok=True)
            print(f"Pasta '{nome_pasta}' criada com sucesso!")
        except Exception as e:
            print(f"Erro ao criar pasta: {e}")
    else:
        print("Comando não reconhecido.")

# Exemplos:
executar_comando("criar pasta Relatórios")
executar_comando("nova pasta Teste2025")
