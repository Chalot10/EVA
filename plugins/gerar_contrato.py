# plugins/gerar_contrato.py
from docx import Document
from docx.shared import Pt
import os


def executar(parametro, assistente):
    """Gera contrato a partir de template"""
    # Formato: "Nome do Cliente | Valor | Data"
    partes = parametro.split("|")

    if len(partes) < 2:
        assistente.falar("Formato: nome | valor")
        return

    nome = partes[0].strip()
    valor = partes[1].strip()

    doc = Document()
    doc.add_heading('CONTRATO DE PRESTAÇÃO DE SERVIÇOS', 0)

    doc.add_paragraph(f'Cliente: {nome}')
    doc.add_paragraph(f'Valor: {valor}€')
    doc.add_paragraph(f'Data: {__import__("datetime").date.today()}')

    # Guardar
    pasta = os.path.expanduser("~/Documentos/Contratos")
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, f"contrato_{nome.replace(' ', '_')}.docx")
    doc.save(caminho)

    assistente.falar(f"Contrato gerado: {caminho}")