import os
import time
import speech_recognition as sr  # включает в себя google speech recognition API
from fuzzywuzzy import fuzz  # модуль для нечеткого сравнения
import pyttsx3  # преобразование текста в речь (для windows сначала: pywin32 224 pypiwin32 223
import datetime  # PyAudio для считывания с микрофона

from datetime import datetime

import pyttsx3
import time

"""проверка говорилки"""
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')  # объявляем пак голосов
# for voi in voices:
#     print(voi)
# engine.setProperty('voice', voices[0].id)  # выбираем голос
# engine.setProperty('rate', 175)  # скорость
# engine.say('Привет, я Лана')
# engine.runAndWait()
# engine.say('Привет, я Лана')
# engine.runAndWait()

"""узнаю индекс микрофона"""
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

"""тест распознавания"""
# recog = sr.Recognizer()
# with sr.Microphone(device_index=1) as source:
#     print('Say!')
#     audio = recog.listen(source)
#
# query = recog.recognize_google(audio, language='ru-RU')
# print('ты сказал: ' + query.lower())
#

# «Говорящие часы» — программа озвучивает системное время

tts = pyttsx3.init()

tts.setProperty('voice', 'ru')  # Наш голос по умолчанию

tts.setProperty('rate', 150)    # Скорость в % (может быть > 100)

tts.setProperty('volume', 0.8)  # Громкость (значение от 0 до 1)

def set_voice(): # Найти и выбрать нужный голос по имени

    voices = tts.getProperty('voices')

    for voice in voices:

        if voice.name == 'Aleksandr':

           tts.setProperty('voice', voice.id)

        else:

            pass

def say_time(msg): # Функция, которая будет называть время в заданном формате

    set_voice() # Настроить голос

    tts.say(msg)
    print('RaW starts')
    tts.runAndWait()  # Воспроизвести очередь реплик и дождаться окончания речи
    print('RaW ended')

while True:

    time_checker = datetime.now() # Получаем текущее время с помощью datetime
    params = [x for x in range(0, 50, 10)]
    if time_checker.second in params:

        say_time('{h} {m}'.format(h=time_checker.hour, m=time_checker.minute))

        time.sleep(5)

    else:

        pass
