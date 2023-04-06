from gtts import gTTS
import pygame
pygame.mixer.init(devicename="Speakers (Realtek(R) Audio)")


def speak(text):
    tts = gTTS(text, lang='en')
    tts.save("s.mp3")
    pygame.mixer.music.load("s.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.get_busy():
        continue
    


