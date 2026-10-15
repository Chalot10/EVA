class Router:
    def __init__(self, assistente):
        self.assistente = assistente
        # Aqui vamos adicionar a integração com IA posteriormente

    def processar(self, comando):
        """
        Processa o comando e decide qual sistema usar:
        - Comandos tradicionais
        - LLM
        - Algoritmos de IA
        """
        # Por enquanto, apenas retorna False para usar o sistema tradicional
        # Futuramente, aqui será a lógica de decisão
        return False

    def processar_com_llm(self, comando):
        """Processa o comando usando LLM"""
        # Implementação futura
        pass

    def processar_com_algoritmo(self, comando):
        """Processa o comando usando algoritmos de IA"""
        # Implementação futura
        pass