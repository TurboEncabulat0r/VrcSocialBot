from gtts import gTTS
import pygame
# Line (VB-Audio Virtual Cable)
# Speakers (2- Realtek(R) Audio)
pygame.mixer.init()


def speak(text):
    pygame.mixer.music.unload()
    tts = gTTS(text, lang='en')
    tts.save('data/s.mp3')

    pygame.mixer.music.load("data/s.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.get_busy():
        continue

    


