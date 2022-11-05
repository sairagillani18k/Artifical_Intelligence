from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
#speech = gTTS(text="Hey Guys! Thanks for watching", lang=language)
speech = gTTS(text="Every good deed is charity. The Prophet Muhammad (Peace Be Upon Him)", lang=language)

speech.save(audio)
playsound("speech.mp3")
