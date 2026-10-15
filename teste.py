from gtts import gTTS
import pyglet
import os

def falar(texto):
    try:
        arquivo_temp = "fala_temp.mp3"
        # slow=True deixa a fala mais lenta
        tts = gTTS(texto, lang='pt', slow=True)
        tts.save(arquivo_temp)

        # Reproduz com pyglet
        som = pyglet.media.load(arquivo_temp, streaming=False)
        player = pyglet.media.Player()
        player.queue(som)
        player.play()

        # Espera terminar antes de continuar
        while player.playing:
            pyglet.app.platform_event_loop.dispatch_posted_events()

        os.remove(arquivo_temp)
    except Exception as e:
        print(f"Erro ao falar: {e}")

# Exemplo de uso
falar("Olá! Esta frase será falada mais devagar.")

# --- Exemplo de uso ---
if __name__ == "__main__":
    falador = Fala()
    falador.falar("Mensagem FBN")
    for i in range(5):
        falador.falar(f"Mensagem número {i}")

    # Espera até todas as falas terminarem
    falador.fila.join()
