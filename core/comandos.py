import json


class GerenciadorComandos:
    def __init__(self, comandos_file="comandos.json"):
        self.comandos_file = comandos_file
        self.comandos = []
        self.carregar_comandos()

    def carregar_comandos(self):
        """Carrega os comandos do arquivo JSON"""
        try:
            with open(self.comandos_file, "r", encoding="utf-8") as f:
                self.comandos = json.load(f)["comandos"]
        except FileNotFoundError:
            print(f"Arquivo {self.comandos_file} não encontrado")
            self.comandos = []
        except json.JSONDecodeError:
            print(f"Erro ao decodificar {self.comandos_file}")
            self.comandos = []

    def processar_comando(self, comando, assistente):
        """Processa um comando usando o sistema tradicional de comandos"""
        if not comando:
            return

        for categoria in self.comandos:
            for key, lista_comandos in categoria.items():
                for item in lista_comandos:
                    for frase, detalhe in item.items():
                        if isinstance(detalhe, dict):
                            func_path = detalhe.get("acao")
                            resposta = detalhe.get("resposta", "")

                            # Comando com wildcard (*)
                            if "*" in frase:
                                base = frase.replace("*", "").strip()
                                if comando.startswith(base):
                                    parametro = comando[len(base):].strip()
                                    assistente.executor.executar(func_path, parametro)
                                    if resposta:
                                        assistente.falar(resposta.replace("{param}", parametro))
                                    return

                            # Comando exato
                            elif frase == comando:
                                assistente.executor.executar(func_path)
                                if resposta:
                                    assistente.falar(resposta)
                                return

        assistente.falar("Desculpe, não entendi o comando.")