import SpeechToText
import aiText
import TextToSpeech
import discord
from discord.ext import commands
import keyboard as kb
import mouse
import time

bot = commands.Bot(command_prefix='.')

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


@bot.event()
async def on_ready():
    print("Bot is ready")


@bot.command(name="walk", brief="Make the bot walk in a specified direction")
async def walk(ctx):
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
    content = ctx.message.content
    cmds = breakString(content)

    if len(cmds) == 1:
        await ctx.send("Please specify a message to say")
        return

    message = cmds[1]
    TextToSpeech.speak(message)


@bot.command(name="rotate", brief="Make the bot rotate in a specified direction")
async def rotate(ctx):
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
    else:
        mouse.move(dist, 0, absolute=False, duration=1)


def botDelegate():
    while True:
        try:
            convo = SpeechToText.speechToText()
        except:
            pass


def main():
    bot.run("token")







