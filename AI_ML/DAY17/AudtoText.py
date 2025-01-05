import pyaudio
import speech_recognition as sr
rec=sr.Recognizer()

with sr.Microphone() as src:
    print('Say Something......')
    rec.adjust_for_ambient_noise(src)
    audio=rec.listen(src)

try:
    txt=rec.recognize_google(audio)
    print(txt)
except sr.UnknownValueError:
    print('could not understand audio')
except sr.RequestError as e:
    print(e)