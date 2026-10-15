import os
import vlc
import random


class MusicPlayer:
    def __init__(self, pasta_musicas):
        self.pasta = pasta_musicas
        self.musicas = [os.path.join(self.pasta, f) for f in os.listdir(self.pasta)
                        if f.lower().endswith(('.mp3', '.wav', '.flac'))]
        if not self.musicas:
            raise Exception("Nenhuma música encontrada na pasta")

        self.index = 0
        self.player = vlc.MediaPlayer(self.musicas[self.index])

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def next_track(self):
        self.index = (self.index + 1) % len(self.musicas)
        self.player.stop()
        self.player = vlc.MediaPlayer(self.musicas[self.index])
        self.player.play()

    def prev_track(self):
        self.index = (self.index - 1) % len(self.musicas)
        self.player.stop()
        self.player = vlc.MediaPlayer(self.musicas[self.index])
        self.player.play()

    def play_all(self):
        while True:
            self.play()
            while self.player.is_playing():
                pass  # espera terminar
            self.next_track()
