import os
import openai
import json
from helpers import *
model_id = 'gpt-3.5-turbo'
conversation = []
total_tokens = 0
token = ""
org = ""

def init():
    global token, org
    logger.log(f"token{token}", "i")
    openai.organization = org
    openai.api_key = token

def setToken(t, o):
    global token, org
    logger.log(f"setting token to {t}", "i")
    token = t
    org = o

def saveConversation():
    logger.log("saving conversation", "i")
    with open("data/conv.txt", "w") as f:
        json.dump(conversation, f)

def loadConversation():
    global conversation
    logger.log("loading conversation", "i")
    with open("data/conv.txt", "r") as f:
        conversation = json.load(f)

def initialiseConvo(prompt):
    getResponse(prompt)
    logger.log("conversation init", "i")

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    api_usage = response['usage']
    logger.log(f'GPT response received, Total token consumed: {api_usage["total_tokens"]}', 'i')
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

def getResponse(prompt):
    global conversation
    logger.log("getting gpt response", "i")
    if token == "":
        return "no openai token"
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)

    return conversation[-1]['content']

try:
    loadConversation()
except:
    pass





