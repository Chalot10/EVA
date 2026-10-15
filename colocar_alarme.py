import threading
import time
from pydub.playback import play
from pydub import AudioSegment
import re
from datetime import datetime, timedelta

# Configurações
unities_to_secs = {"horas": 3600, "hora": 3600, "minuto": 60, "minutos": 60, "segundos": 1, "segundo": 1}
ALARM_SOUND = AudioSegment.from_wav("modules/alarm.wav")


class CountdownTask:
    def __init__(self, purpose, assistente=None):
        self._running = True
        self.purpose = purpose
        self.assistente = assistente

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            n -= 1
            time.sleep(1)
        else:
            if self._running:  # Só toca se não foi cancelado
                try:
                    play(ALARM_SOUND)
                    if self.assistente:
                        self.assistente.falar("Está na hora de lembrar de " + self.purpose)
                    print(f"ALARME: {self.purpose}")
                except:
                    if self.assistente:
                        self.assistente.falar("Hora do alarme: " + self.purpose)


def parse_command(command_action, argument, when, assistente=None):
    """Processa comandos de alarme"""
    print(f"ALARM_MODULE - Comando: {command_action}, Argumento: '{argument}', Quando: '{when}'")

    if len(when) == 0:
        if assistente:
            assistente.falar("Por favor, especifique o tempo para o alarme")
        return

    if command_action['type'] == 'in':
        text = when
        if when.startswith('a'):
            text = when[1:].strip()

        seconds = text2seconds(text)
        if seconds > 0:
            set_alarm_in(seconds, argument, assistente)
            timeToAlarm = (datetime.now() + timedelta(seconds=seconds)).strftime("%H:%M")
            if assistente:
                assistente.falar(f"Alarme anotado para às {timeToAlarm}")
        else:
            if assistente:
                assistente.falar("Não consegui entender o tempo do alarme")


def text2seconds(text):
    """Converte texto para segundos"""
    try:
        if ':' in text:  # Formato hh:mm
            from time import strptime
            time_obj = strptime(text.strip(), '%H:%M')
            return (time_obj.tm_hour * 3600) + (time_obj.tm_min * 60)
        else:
            result = 0
            words = text.split(' ')

            # Importar text2int localmente para evitar dependência circular
            try:
                from utils.text2int import text2int
            except:
                # Fallback simples se text2int não estiver disponível
                def text2int(word):
                    numeros = {
                        "um": 1, "dois": 2, "três": 3, "quatro": 4, "cinco": 5,
                        "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10,
                        "onze": 11, "doze": 12, "treze": 13, "catorze": 14, "quinze": 15,
                        "dezesseis": 16, "dezessete": 17, "dezoito": 18, "dezenove": 19,
                        "vinte": 20, "trinta": 30, "quarenta": 40, "cinquenta": 50,
                        "sessenta": 60
                    }
                    return numeros.get(word.lower(), 0)

            for index, word in enumerate(words):
                if word in unities_to_secs:
                    number = 0
                    if index > 0 and words[index - 1].isnumeric():
                        number = int(words[index - 1])
                    else:
                        number = text2int(words[index - 1].strip()) if index > 0 else 1

                    result += unities_to_secs[word] * number

            # Verifica números sem unidade
            for word in words:
                if word.isnumeric():
                    result += int(word)

            if 'e meia' in text:
                result += 1800
            if 'meia hora' in text:
                result += 1800

            return result
    except Exception as e:
        print(f"Erro em text2seconds: {e}")
        return 0


def set_alarm_in(seconds, argument, assistente=None):
    """Configura um alarme"""
    c = CountdownTask(argument, assistente)
    t = threading.Thread(target=c.run, args=(seconds,), daemon=False)
    t.start()
    print(f'Alarme iniciado: {seconds} segundos para "{argument}"')


def extract_argument_with_time(command_text, voice_command, time_indicator):
    """Extrai argumento e tempo do comando de voz"""
    regex_time_indicator = rf"\b{time_indicator}\b"
    time_indicator_pos = -1

    time_indicator_search = re.search(regex_time_indicator, command_text)
    if time_indicator_search is not None:
        time_indicator_pos = time_indicator_search.start()

    if time_indicator_pos == -1:
        return ['', '']

    when = command_text[time_indicator_pos + len(time_indicator):].strip()
    command_text_without_when = command_text[:time_indicator_pos].strip()

    voice_command_without_when = ''
    time_indicator_voice_command_search = re.search(regex_time_indicator, voice_command)
    if time_indicator_voice_command_search is not None:
        voice_command_without_when = voice_command[:time_indicator_voice_command_search.start()].strip()

    splitted_text = command_text_without_when.split(voice_command_without_when.replace('*', ''), 1)

    argument = splitted_text[1] if len(splitted_text) > 1 else splitted_text[0]

    return [argument.strip(), when.strip()]