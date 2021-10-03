import speech_recognition as sr

audio = ('song.wav')

r = sr.Recognizer()

with sr.AudioFile(audio) as source:
    audio = r.record(source)

try:
    print("Audio file contains\n",r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech recognition could not understand audio")
except sr.RequestError:
    print("Couldn't get the results")
