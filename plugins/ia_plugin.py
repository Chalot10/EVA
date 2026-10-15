from langchain.chat_models import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Inicializa modelo Ollama phi3
llm = Ollama(model="phi3")
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
conversation = ConversationChain(llm=llm, memory=memory)


def processar_comando_ia(texto, assistente=None):
    """
    Recebe comando de usuário, decide ação e responde
    """
    resposta = conversation.run(texto)

    # Se assistente tiver função de voz
    if assistente:
        assistente.falar(resposta)

    # Aqui a IA pode retornar instruções que você parseia para chamar plugins
    # Exemplo: "abrir word e escrever teste" -> você chama word_plugin
    return resposta
