import webbrowser
from assistente import Assistente

assistente = Assistente()



def google():
    assistente.falar("Abrindo o google")
    webbrowser.open("https://www.google.com")

def youtube():
    assistente.falar("Abrindo o youtube")
    webbrowser.open("https://www.youtube.com")

def bing():
    assistente.falar("Abrindo o bing")
    webbrowser.open("https://www.bing.com")

def gemail():
    assistente.falar("Abrindo o gmail")
    webbrowser.open("https://www.gmail.com")

def spotify():
    # assistente.falar("Abrindo o bing")
    webbrowser.open("https://www.spotify.com")

def twitter():
    # assistente.falar("Abrindo o twitter")
    webbrowser.open("https://www.twitter.com")

def instagram():
    assistente.falar("Abrindo o instagram")
    webbrowser.open("https://www.instagram.com")

# def facebook():
#     assistente.falar("Abrindo o facebook")
#     webbrowser.open("https://www.facebook.com")
#
# def facebook():
#     assistente.falar("Abrindo o facebook")
#     webbrowser.open("https://www.facebook.com")
