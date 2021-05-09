import speech_recognition as sr
import pyttsx3,sys

text = 'Привет, как дела?'
tts = pyttsx3.init()
rate = tts.getProperty('rate') #Скорость произношения
tts.setProperty('rate', rate-40)

volume = tts.getProperty('volume') #Громкость голоса
tts.setProperty('volume', volume+0.9)

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)

def say(text):
    tts.say(text)
    tts.runAndWait()

def record_volume(tts):
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        print('Слушаю...')
        audio = r.listen(source)
    print('Услышала.')

    commandList = {
        'привет' : 'Сам привет!',
        'как дела' : 'отлично, а у тебя как?',
        'нормально' : 'Ок',
        'здорово' : 'пойдёт',
        'круто' : 'нормально',
        'ладно' : 'ок ладно',
        'что ты умеешь' : 'Я умею пока отвечать на вопрос, "как дела?"',
    }
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        text = query.lower()
        print(f'Вы сказали: {text}')

        if 'сайт' in text:
            
        elif  text in commandList:
            commandList[text]
            say(commandList[text])
        else:
            say(f'Вы сказали: {text}')
    except:
        print('Error')

while True:
    record_volume(tts)