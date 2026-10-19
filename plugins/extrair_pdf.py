from pdfminer.high_level import extract_text
import os


def executar(parametro, assistente):
    """Extrai texto de um PDF"""
    if not parametro or not os.path.exists(parametro):
        assistente.falar("PDF não encontrado")
        return

    try:
        texto = extract_text(parametro)
        # Guardar em txt
        saida = parametro.replace(".pdf", ".txt")
        with open(saida, "w", encoding="utf-8") as f:
            f.write(texto)
        assistente.falar(f"Texto extraído para {saida}")
    except Exception as e:
        assistente.falar(f"Erro ao extrair: {e}")