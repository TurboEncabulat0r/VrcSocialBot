import os
import openai
import json
openai.organization = "org-mbxkzhcXlJKPxAmQUmMhUdBT"
openai.api_key = "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"

model_id = 'gpt-3.5-turbo'
conversation = []

def saveConversation():
    with open("conv.txt", "w") as f:
        json.dump(conversation, f)

def loadConversation():
    global conversation
    with open("conv.txt", "r") as f:
        conversation = json.load(f)

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    api_usage = response['usage']
    print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

def getResponse(prompt):
    global conversation
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)

    return conversation[-1]['content']

try:
    loadConversation()
except:
    pass





