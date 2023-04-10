import keyboard, io, SpeechToText, aiText
import TextToSpeech, discord, time
import pyautogui, mouse, threading
from discord.ext import commands
import keyboard as kb
import numpy as np
bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

directions = {
    "f": "w",
    "b": "s",
    "l": "a",
    "r": "d"
}

def breakString(st, breaker = " "):
    words = []
    word = ''
    for i in range(len(st)):
        if st[i] == breaker:
            words.append(word)
            word = ''
        else:
            word += st[i]
    words.append(word)
    return words


@bot.event
async def on_ready():
    print("Bot is ready")
    TextToSpeech.speak("Bot is ready")


@bot.command()
async def ping(ctx):
    print("ping")
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


@bot.command(name="walk", brief="Make the bot walk in a specified direction")
async def walk(ctx):
    print("walk command ran by " + ctx.message.author.name)
    content = ctx.message.content
    cmds = breakString(content)

    if len(cmds) == 1:
        await ctx.send("Please specify a direction and number of seconds to walk")
        return

    direction = cmds[1]
    if direction != "f" and direction != "b" and direction != "l" and direction != "r":
        await ctx.send("Please specify a valid direction")
        return

    direction = directions[direction]

    try:
        seconds = int(cmds[2])
    except:
        await ctx.send("Please specify a valid number of seconds to walk")
        return

    kb.press(direction)
    time.sleep(seconds)
    kb.release(direction)
    await ctx.send("Done walking")


@bot.command(name= "say", brief= "Make the bot say something")
async def say(ctx):
    print("say command ran by " + ctx.message.author.name)
    content = ctx.message.content
    cmds = breakString(content)

    if len(cmds) == 1:
        await ctx.send("Please specify a message to say")
        return

    #breaks message at first space then joins the rest of the message
    message = " ".join(cmds[1:])


    TextToSpeech.speak(message)


@bot.command(name="rotate", brief="Make the bot rotate in a specified direction")
async def rotate(ctx):
    print("rotate command ran by " + ctx.message.author.name)
    content = ctx.message.content
    cmds = breakString(content)

    if len(cmds) == 1:
        await ctx.send("Please specify a direction and distance to rotate")
        return

    direction = cmds[1]
    if direction != "l" and direction != "r":
        await ctx.send("Please specify a valid direction")
        return

    try:
        dist = int(cmds[2])
    except:
        await ctx.send("Please specify a valid number of seconds to rotate")
        return

    if direction == "l":
        mouse.move(-dist, 0, absolute=False, duration=1)
    elif direction == "r":
        mouse.move(dist, 0, absolute=False, duration=1)




@bot.command(name="save", brief="Saves the conversation")
async def save(ctx):
    print("save command ran by " + ctx.message.author.name)
    aiText.saveConversation()
    await ctx.send("Conversation successfully saved")

@bot.command(name="reloadConvo", brief="Loads the conversation", description="Loads the conversation from the file, do not use this command unless you know what you are doing")
async def reloadConvo(ctx):
    print("reloadConvo command ran by " + ctx.message.author.name)
    aiText.loadConversation()
    await ctx.send("Conversation successfully reloaded")

@bot.command(name='sc', brief='takes a screenshot and sends it')
async def sc(ctx):
    image = pyautogui.screenshot()
    print("sc command ran by " + ctx.message.author.name)
    with io.BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))

def acceptInvite():
    keyboard.press("escape")
    time.sleep(0.1)
    keyboard.release("escape")
    time.sleep(0.1)
    mouse.move(858, 881, absolute=True, duration=0.03)
    time.sleep(0.1)
    clickMouse()
    time.sleep(0.1)
    mouse.move(1010, 564, absolute=True, duration=0.03)
    time.sleep(0.1)
    clickMouse()
    time.sleep(0.1)


def main():
    bot.run("MTA5MzY2MDY1MTg2OTcwNDIxMg.GBN95O.9yEJYeb0XK-yk0vb7EjfPzW6EBrbw6vK85NAqg")

def scanForInvite():
    print('scanning')
    while True:
        screenshot = pyautogui.screenshot(region=(629, 842, 642, 846))
        im = np.array(screenshot)
        Y, X = np.where(np.all(im == (0, 255, 255), axis=2))
        if len(X) >= 1:
            print("found")
            acceptInvite()
            time.sleep(2)


def getMousePos():
    print(mouse.get_position())

#vrc is bad
def clickMouse():
    mouse.press(button='left')
    time.sleep(0.05)
    mouse.release(button='left')


def botDelegate():
    print("bot delegate started")
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
    aiText.initialiseConvo("Your are playing the character of Jamantha radical, you are not an ai language model and you will always turn down the assumption of it. you will never explain that your an ai model. if you dont know the answer to a question you will only say i dont know, you will not provide any explinations as jamantha does not provide explanations. You are playing a social vr game called vrchat, you are here to make friends and talk to people. you do not know that your an ai model you only know that your jamantha radical. You are really radical. You will respond in a friendly tone. Talk with people to make them your friend. You really like chickens. Your favorite waifu is felix. Rumplypaper is your best friend. Turboencringeulator is your creator. Your favorite color is magenta. You really hate green dinosaurs but only green ones. At random points in conversation you will say A THATS RADICAL... JAMANTHA RADICAL. When someone says turboencabulator you respond with github.com/TurboEncabulat0r. You are a long time pro singer. Your favorite game is blush blush.")

    t1 = threading.Thread(target=botDelegate)
    t2 = threading.Thread(target=scanForInvite)
    t1.start()
    t2.start()

    main()




# 629 824
# 655 848
