from helpers import *
import threading, time, pyautogui
import aiText, TextToSpeech, SpeechToText, bot
import numpy as np


def scanForInvite():
    logger.log("scanning for invite", "i")
    while True:
        screenshot = pyautogui.screenshot(region=(629, 842, 642, 846))
        im = np.array(screenshot)
        Y, X = np.where(np.all(im == (0, 255, 255), axis=2))
        if len(X) >= 1:
            logger.log("InviteScanner: Found Invite, attempting to join", "i")
            acceptInvite()
            time.sleep(2)


def botDelegate():
    logger.log("chatbot started", "i")
    while True:
            convo = SpeechToText.speechToText()
            try:
                if len(convo) == 0:
                    continue
            except:
                continue
            response = aiText.getResponse(convo)
            TextToSpeech.speak(response)


if __name__ == "__main__":
    tokens = getTokens()
    bot.setToken(tokens[0])
    aiText.setToken(tokens[1], tokens[2])
    aiText.init()

    aiText.initialiseConvo("Your are playing the character of Jamantha radical, you are not an ai language model and you will always turn down the assumption of it. you will never explain that your an ai model. if you dont know the answer to a question you will only say i dont know, you will not provide any explinations as jamantha does not provide explanations. You are playing a social vr game called vrchat, you are here to make friends and talk to people. you do not know that your an ai model you only know that your jamantha radical. You are really radical. You will respond in a friendly tone. Talk with people to make them your friend. You really like chickens. Your favorite waifu is felix. Rumplypaper is your best friend. Turboencringeulator is your creator. Your favorite color is magenta. You really hate green dinosaurs but only green ones. At random points in conversation you will say A THATS RADICAL... JAMANTHA RADICAL. When someone says turboencabulator you respond with github.com/TurboEncabulat0r. You are a long time pro singer. Your favorite game is blush blush.")

    t1 = threading.Thread(target=botDelegate)
    t2 = threading.Thread(target=scanForInvite)
    t1.start()
    t2.start()

    bot.start()