from voz.ouvir import ReconhecedorVoz
from voz.falar import SintetizadorVoz
from core.comandos import GerenciadorComandos
from core.router import Router
from core.executor import Executor


class Assistente:
    def __init__(self, comandos_file="comandos.json"):
        # Inicializa os módulos de voz
        self.ouvido = ReconhecedorVoz()
        self.voz = SintetizadorVoz()

        # Inicializa o gerenciador de comandos
        self.comandos = GerenciadorComandos(comandos_file)

        # Inicializa o executor (passa a referência do assistente)
        self.executor = Executor(self)

        # Inicializa o router
        self.router = Router(self)

    def falar(self, texto):
        """Fala um texto usando o sintetizador de voz"""
        self.voz.falar(texto)

    def ouvir(self):
        """Ouve um comando de voz"""
        return self.ouvido.ouvir()

    def processar_comando(self, comando):
        """Processa um comando de texto"""
        if not comando:
            return

        comando = comando.lower().strip()

        # Usa o router para processar o comando
        resultado = self.router.processar(comando)

        # Se o router não processou, tenta o método tradicional
        if not resultado:
            self.comandos.processar_comando(comando, self)

    def executar(self):
        """Loop principal da assistente"""
        self.falar("Olá! Sou a Yuni, sua assistente.")
        self.falar("Em que posso ajudar?")

        while True:
            try:
                comando = self.ouvir()
                if comando and comando.strip():
                    self.processar_comando(comando)
            except KeyboardInterrupt:
                self.falar("Encerrando a Yuni. Até logo!")
                break
            except Exception as e:
                print(f"Erro inesperado: {e}")
                continue