#pip install gtts,playsound

import os
from gtts import gTTS
import playsound


filename=f'{os.getcwd()}\\temp.mp3'
print("Audio File name is :",filename)

say="how are you brother"
language="en"
accent="co.in"

tts=gTTS(text=say,lang=language,tld=accent)
tts.save(filename)

if os.path.exists(filename):
    playsound.playsound(filename)
    os.remove(filename)
