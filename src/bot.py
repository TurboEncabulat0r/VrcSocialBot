import io, aiText
from helpers import *
import TextToSpeech, discord, time
import pyautogui, mouse
from discord.ext import commands
import keyboard as kb

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

token = ""

directions = {
    "f": "w",
    "b": "s",
    "l": "a",
    "r": "d"
}

isRecording = False
activeMacro = None
macros = []

exampleMacro = [{"name": "example", "commands": {"w": 1, "d": 2},"author": "RumplyPaper"}, {"name": "example2", "commands": {"w": 1, "d": 2},"author": "RumplyPaper"}]

            
@bot.event
async def on_ready():
    logger.log("Bot is ready", "i")


@bot.command(brief="returns the bots ping")
async def ping(ctx):
    await ctx.send(f'ping: {round(bot.latency * 1000)}ms')


@bot.command(name="walk", brief="Make the bot walk in a specified direction")
async def walk(ctx):  
    logger.log("walk command ran by " + ctx.message.author.name, "i")
    content = ctx.message.content
    cmds = breakString(content)

    if len(cmds) == 1:
        await ctx.send("Please specify a direction and number of seconds to walk")
        return

    direction = cmds[1]
    if direction != "f" and direction != "b" and direction != "l" and direction != "r":
        await ctx.send("Please specify a valid direction")
        return

    dir = directions[direction]

    try:
        seconds = int(cmds[2])
    except:
        await ctx.send("Please specify a valid number of seconds to walk")
        return
    
    if isRecording:
        activeMacro.commands.Append({direction: seconds})

    kb.press(dir)
    time.sleep(seconds)
    kb.release(dir)
    await ctx.send("Done walking")


@bot.command(name= "say", brief= "Make the bot say something")
async def say(ctx):
    
    content = ctx.message.content
    cmds = breakString(content)

    if len(cmds) == 1:
        await ctx.send("Please specify a message to say")
        return

    message = "".join(cmds[1:])
    
    logger.log("say command ran by " + ctx.message.author.name + " with message of " + message, "i")

    TextToSpeech.speak(message)


@bot.command(name="rotate", brief="Make the bot rotate in a specified direction")
async def rotate(ctx):
    logger.log("rotate command ran by " + ctx.message.author.name, "i")
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
    
    if isRecording:
        activeMacro.commands.Append({direction: dist})

    if direction == "l":
        mouse.move(-dist, 0, absolute=False, duration=1)
    elif direction == "r":
        mouse.move(dist, 0, absolute=False, duration=1)



@bot.command(name="saveAIState", brief="Saves the conversation")
async def saveAIState(ctx):
    logger.log("saveAIState ran by " + ctx.message.author.name, "i")
    aiText.saveConversation()
    await ctx.send("Conversation successfully saved")


@bot.command(name="reloadAIState", brief="Loads the conversation", description="Loads the conversation from the file, do not use this command unless you know what you are doing")
async def reloadAIState(ctx):
    logger.log("reloadAIState command ran by " + ctx.message.author.name, "i")
    
    aiText.loadConversation()
    await ctx.send("Conversation successfully reloaded")


@bot.command(name='sc', brief='takes a screenshot and sends it')
async def sc(ctx):
    image = pyautogui.screenshot()
    logger.log("sc command ran by " + ctx.message.author.name, "i")
    with io.BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))


@bot.command(brief="stops recording the macro")
async def stopRecording(ctx):
    isRecording = False
    await ctx.send("Recording stopped")


@bot.command()
async def startRecording(ctx):
    isRecording = True

    if (activeMacro != None):
        activeMacro = None
    activeMacro = Macro(None, ctx.message.author.name)

    await ctx.send("Recording started")


@bot.command(brief="saves the active macro")
async def saveMacro(ctx):
    if activeMacro == None:
        await ctx.send("No active macro")
        return
    isRecording = False

    
    macros.append(activeMacro)
    activeMacro = None

    await ctx.send("Macro saved")

@bot.command()
async def playMacro(ctx):
    content = ctx.message.content
    cmds = breakString(content)
    logger.log("playMacro command ran by " + ctx.message.author.name, "i")

    if len(cmds) == 1:
        await ctx.send("Please specify a macro to play")
        return

    name = cmds[1]
    macro = None

    for m in macros:
        if m.name == name:
            macro = m
            break

    if macro == None:
        await ctx.send("Macro not found")
        return

    macro.execute()

def setToken(t):
    global token
    token = t

def start():
    if token == "":
        logger.log("Token not set", "e")
        return
    bot.run(token)