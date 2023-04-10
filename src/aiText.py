import os
import openai
import json
openai.organization = "org-mbxkzhcXlJKPxAmQUmMhUdBT"
openai.api_key = "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"

model_id = 'gpt-3.5-turbo'
conversation = []
total_tokens = 0

def saveConversation():
    with open("data/conv.txt", "w") as f:
        json.dump(conversation, f)

def loadConversation():
    global conversation
    with open("data/conv.txt", "r") as f:
        conversation = json.load(f)

def initialiseConvo(prompt):
    getResponse(prompt)

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    api_usage = response['usage']
    print(f'GPT response received, Total token consumed: {api_usage["total_tokens"]}')
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

def getResponse(prompt):
    global conversation
    print("getting gpt response")
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)

    return conversation[-1]['content']

try:
    loadConversation()
except:
    pass





