# import os
import time
# import datetime
import pyaimp as pa
import pyttsx3  # преобразование текста в речь (для windows сначала: pywin32 224 pypiwin32 223)
import speech_recognition as sr  # включает в себя google speech recognition. # PyAudio для считывания с микрофона
from fuzzywuzzy import fuzz  # модуль для нечеткого сравнения

"""Settings"""
options = {
    "names": ('лана', 'детка', 'ладно', 'котик', 'хотя', 'ты', 'она', 'ланочка', 'поночка', 'ванночка'),
    "tbr": ('скажи', 'расскажи', 'сделаешь', 'покажи', 'сколько', 'сделай', 'давай', 'произнеси', 'твою', 'свою',
            'любимую', 'сначала', 'мне'),  # to be removed
    "commands": {
        "ctime": ('текущее время', 'сейчас времени', 'который час'),
        # "radio": ('включи музыку', 'воспроизведи радио', 'включи радио'),
        "aimp_play": ('спой', 'споём', 'продолжай'),
        "aimp_pause": ('погоди', 'постой'),
        "mk_drink": ('кофе', 'чай')
    }
}

"""Functions"""


class SpeakerClass:

    def __init__(self):
        self.engine = pyttsx3.init()

    def says(self, text_):
        self.engine.say(text_)
        self.engine.runAndWait()


def speak(text):  # говорилка
    print(text)
    speaker = SpeakerClass()
    speaker.says(text)
    del speaker


def callback(recognize, audio):
    try:
        recorded_voice = recognize.recognize_google(audio, language="ru-RU").lower()
        print("Распознано: " + recorded_voice)

        if recorded_voice.startswith(options["names"]):  # если начинается с имени
            command = recorded_voice

            for x in options['names']:  # Выделяем комманду
                command = command.replace(x, "").strip()
            for x in options['tbr']:
                command = command.replace(x, "").strip()

            command = recognize_command(command)  # распознаем и выполняем команду
            execute_command(command['commands'])

    except sr.UnknownValueError:
        print("Голос не распознан!")
    except sr.RequestError as e:
        print("Неизвестная ошибка, проверьте интернет!", e)


def recognize_command(command):  # нечеткое сравнение записи с вариантами комманд
    rec_cmd = {'commands': '', 'percent': 0}
    for cmd, var in options['commands'].items():
        for v in var:
            vrt = fuzz.ratio(command, v)
            if vrt > rec_cmd['percent']:  # Выбор наилучшей
                rec_cmd['commands'] = cmd
                rec_cmd['percent'] = vrt
    return rec_cmd


def execute_command(command):
    # print(command)
    # if command == 'ctime':
    # сказать текущее время
    # now = datetime.datetime.now()
    # speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    # elif command == 'radio':
    # воспроизвести музыку
    # os.startfile("E:\\Music\\Подборки\\18 Spring\\ALEX - Youth (feat. Rachel McAlpine).mp3")
    if command == 'mk_drink':
        # сделай
        speak("Я бы с радостью лапа ... Как только сделаешь мне ручки")
    elif command == 'aimp_play':
        aimp.play()
        aimp.set_volume(15)
    elif command == 'aimp_pause':
        aimp.pause()
        speak('да да')
    else:
        print('Команда не распознана, повторите!')


"""Start"""
recognizer = sr.Recognizer()  # объявляем рекогнайзер
micro = sr.Microphone(device_index=1)  # объявляем микрофон

#  aimp
aimp = pa.Client()

with micro as source:
    recognizer.adjust_for_ambient_noise(source)  # слушает шум секунду

# speaker = pyttsx3.init()  # # объявляем говорилку
# voices = speaker.getProperty('voices')  # объявляем пак голосов
# speaker.setProperty('voice', voices[2].id)  # выбираем голос

speak('Привет сладкий. Я скучала')  # Приветствие

stop_listening = recognizer.listen_in_background(micro, callback)  # начинает слушать

while True:
    time.sleep(0.1)  # infinity loop
