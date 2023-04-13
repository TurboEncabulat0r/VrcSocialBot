import json, time, mouse, os
import keyboard as kb


class logging():
    def __init__(self):
        
        self.runtime = time.time()

        self.isVerbose = True
        self._log = []

    def log(self, message, type = "i"):
        msg = ""
        if type == "i":
            msg = f"[INFO] {message}"
        elif type == "w":
            msg = f"[WARN] {message}"
        elif type == "e":
            msg = f"[ERROR] {message}"
        else:
            msg = f"[UNKNOWN] {message}"

        if self.isVerbose:
            print(msg)
        self._log.append(msg)


    def dumpLog(self):
        if self.isVerbose:
            print("Dumping log")
        with open(f"logs/{int(runtime)}.log", "w") as f:
            for msg in self.log:
                f.write(time.strftime("%H:%M:%S") + " " + msg)
        

    def setVerbose(self, verbose):
        self.isVerbose = verbose

logger = logging()

class Macro():
    def __init__(self, name, author):
        self.name = name
        self.cmds = []
        self.author = author

    def __str__(self):
        return self.name
    
    def getSteps(self):
        return self.commands
    
    def getRaw(self):
        return {"name": self.name, "commands": self.cmds}
    
    def execute(self):
        for cmd in self.cmds:
            for key, value in cmd.items():
                if key == "w" or key == "s" or key == "a" or key == "d":
                    kb.press(key)
                    time.sleep(value)
                    kb.release(key)

                elif key == "l":
                    mouse.move(-value, 0, absolute=False, duration=1)
                elif key == "r":
                    mouse.move(value, 0, absolute=False, duration=1)
                else:
                    logger.log("Invalid command in macro", "e")
                    return
                

def acceptInvite():
    kb.press("escape")
    time.sleep(0.1)
    kb.release("escape")
    time.sleep(0.1)
    mouse.move(858, 881, absolute=True, duration=0.03)
    time.sleep(0.1)
    clickMouse()
    time.sleep(0.1)
    mouse.move(1010, 564, absolute=True, duration=0.03)
    time.sleep(0.1)
    clickMouse()
    time.sleep(0.1)


def getTokens():
    tokens = []
    #gets the tokens from the tokens.txt file located in the users documents folder
    if not os.path.exists(os.path.expanduser('~') + "\Documents\okens.txt"):
        logger.log("Tokens file not found, creating new one", "i")
        disc = input("Enter your discord bot token: ")
        openai = input("Enter your openai token: ")
        org = input("Enter your openai organization id: ")
        with open(os.path.expanduser('~') + "\Documents\okens.txt", "w") as f:
            f.write(disc + "\n" + openai + "\n" + org)
        
        return [disc, openai, org]

    with(open(os.path.expanduser('~') + "\Documents\okens.txt", "r")) as f:
        tokens = f.read().splitlines()

    return tokens


        
def getAllMacros():
    macros = []
    
    if not os.path.exists("macros"):
        os.makedirs("macros")

    files = os.listdir("macros")

    for file in files:
        macro = Macro(file, json.load(open(f"macros/{file}", "r")))
        macros.append(macro)

    return macros
    

def getMousePos():
    print(mouse.get_position())


#vrc is bad
def clickMouse():
    mouse.press(button='left')
    time.sleep(0.05)
    mouse.release(button='left')

def presskey(key, delay = 0.05):
    kb.press(key)
    time.sleep(delay)
    kb.release(key)


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

