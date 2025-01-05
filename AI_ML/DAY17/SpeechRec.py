from gtts import gTTS
import os

word=''

tts=gTTS(text=word,lang='ta')


tts.save("op.mp3")
os.system("start op.mp3")