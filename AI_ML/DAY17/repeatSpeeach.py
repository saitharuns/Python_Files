from gtts import gTTS
import os

while True:
    def tell():
        word=input("text to say : ")
        tts=gTTS(text=word,lang='')
        tts.save("op.mp3")
        os.system("start op.mp3")
    key=int(input("enter 1 to break 2 to rec "))
    if key==1:
        break
    if key==2:
        tell()