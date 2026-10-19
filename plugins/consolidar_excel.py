import pandas as pd
import os
import glob


def executar(parametro, assistente):
    """Consolida todos os Excel de uma pasta"""
    pasta = parametro if parametro else "."
    ficheiros = glob.glob(os.path.join(pasta, "*.xlsx"))

    if not ficheiros:
        assistente.falar("Nenhum ficheiro Excel encontrado")
        return

    dfs = []
    for f in ficheiros:
        df = pd.read_excel(f)
        df['_origem'] = os.path.basename(f)
        dfs.append(df)

    consolidado = pd.concat(dfs, ignore_index=True)
    saida = os.path.join(pasta, "consolidado.xlsx")
    consolidado.to_excel(saida, index=False)

    assistente.falar(f"Consolidados {len(ficheiros)} ficheiros em {saida}")