import wikipedia
from assistente import Assistente


assistente = Assistente()

wikipedia.set_lang("pt")

def pesquisar(termo):
    try:
        assistente.falar("Pesqisando por" + termo)
        resumo = wikipedia.summary(termo, sentences=1)
        print(resumo)
    except Exception:
        assistente.falar("Não encontrei nenhum resultado pesquisado de " + termo)
