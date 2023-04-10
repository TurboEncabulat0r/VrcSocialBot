#this converts speech to text
import speech_recognition as sr
import os

def speechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print("Heard: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        return
    except sr.RequestError as e:
        print("request error")
        return
    except:
        return
    return r.recognize_google(audio)
