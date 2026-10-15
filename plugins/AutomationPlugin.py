import datetime
import json
import uuid
from googletrans import Translator
from fpdf import FPDF

class AutomationPlugin:
    def __init__(self):
        self.tarefas = []
        self.translator = Translator()

    # ---------------- Criar lista de tarefas ----------------
    def adicionar_tarefa(self, descricao):
        tarefa = {"id": str(uuid.uuid4()), "descricao": descricao, "status": "pendente"}
        self.tarefas.append(tarefa)
        return f"Tarefa adicionada: {descricao}"

    def listar_tarefas(self):
        return [f"{t['descricao']} - {t['status']}" for t in self.tarefas]

    def concluir_tarefa(self, tarefa_id):
        for t in self.tarefas:
            if t["id"] == tarefa_id:
                t["status"] = "concluída"
                return f"Tarefa '{t['descricao']}' concluída."
        return "Tarefa não encontrada."

    # ---------------- Gerar ata de reunião ----------------
    def gerar_ata(self, titulo, participantes, decisoes, data=None):
        data = data or datetime.date.today().strftime("%d/%m/%Y")
        ata = {
            "titulo": titulo,
            "data": data,
            "participantes": participantes,
            "decisoes": decisoes
        }
        with open(f"ata_{titulo}.json", "w", encoding="utf-8") as f:
            json.dump(ata, f, ensure_ascii=False, indent=4)
        return f"Ata '{titulo}' gerada com sucesso."

    # ---------------- Transcrever reuniões ----------------
    def transcrever_reuniao(self, audio_file):
        # Aqui você pode integrar Whisper, Vosk ou outro modelo de STT
        texto = f"[Simulação] Transcrição do arquivo {audio_file}"
        return texto

    # ---------------- Preencher formulários automaticamente ----------------
    def preencher_formulario(self, template, dados):
        formulario = template.copy()
        formulario.update(dados)
        return formulario

    # ---------------- Gerar contratos/faturas ----------------
    def gerar_contrato(self, cliente, servico, valor):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, f"CONTRATO DE SERVIÇO\n\nCliente: {cliente}\nServiço: {servico}\nValor: {valor} MZN")
        filename = f"contrato_{cliente}.pdf"
        pdf.output(filename)
        return f"Contrato gerado: {filename}"

    def gerar_fatura(self, cliente, itens):
        total = sum(preco for _, preco in itens)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, f"Fatura para {cliente}", ln=True, align="C")
        for item, preco in itens:
            pdf.cell(0, 10, f"{item}: {preco} MZN", ln=True)
        pdf.cell(0, 10, f"Total: {total} MZN", ln=True)
        filename = f"fatura_{cliente}.pdf"
        pdf.output(filename)
        return f"Fatura gerada: {filename}"

    # ---------------- Integração ERP ----------------
    def integrar_erp(self, sistema, dados):
        # Mock de integração (ex: SAP, Odoo, Primavera)
        return f"Dados enviados para o ERP {sistema}: {dados}"

    # ---------------- Conversão de unidades ----------------
    def converter_unidades(self, valor, de, para):
        if de == "km" and para == "milhas":
            return valor * 0.621371
        elif de == "milhas" and para == "km":
            return valor / 0.621371
        elif de == "kg" and para == "lb":
            return valor * 2.20462
        elif de == "lb" and para == "kg":
            return valor / 2.20462
        else:
            return "Conversão não suportada."

    # ---------------- Traduções rápidas ----------------
    def traduzir(self, texto, destino="en"):
        traducao = self.translator.translate(texto, dest=destino)
        return traducao.text
