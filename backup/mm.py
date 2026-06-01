import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

for v in voices:
    print(v.name)

engine.setProperty('voice', voices[0].id)

engine.say("Testing speech output")
engine.runAndWait()
