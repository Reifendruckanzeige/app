from dotenv import load_dotenv
from prompt import buildMessage
load_dotenv()

import os

import requests as req
import  json

headers = {"Authorization": f"Bearer {os.environ['OPENAI_TOKEN']}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
model_id = "gpt-3.5-turbo"

def generateImage(text):
    endpoint = "https://api.openai.com/v1/images/generations"
    resolution = "256x256"

    message_body = {
        "prompt": text,
        "size": resolution,
    }
    message_body = json.dumps(message_body)

    request = req.post(endpoint, headers=headers, data=message_body)
    ans = request.json()

    return ans["data"][0]["url" ]

def accessGPT(objectName, charLevel):
    message_body = {
        "model": model_id,
        "messages": [{"role": "user", "content": buildMessage(objectName, charLevel)}] 
    }
    message_body = json.dumps(message_body)

    request = req.post(link, headers=headers, data=message_body)
    ans = request.json()

    data = ans["choices"][0]["message"]["content"]

    messageFormatted = data.split("/")

    background = messageFormatted[12].split(": ")[1]

    return {
        "name": messageFormatted[0].split(": ")[1],
        "alignment": messageFormatted[1].split(": ")[1],
        "class": messageFormatted[2].split(": ")[1],
        "race": messageFormatted[3].split(": ")[1],
        "skill": messageFormatted[4].split(": ")[1],
        "weapon": messageFormatted[11].split(": ")[1],
        "attributes": {
            "hp": messageFormatted[5].split(": ")[1], 
            "str": messageFormatted[6].split(": ")[1],
            "dex": messageFormatted[7].split(": ")[1],
            "car": messageFormatted[8].split(": ")[1],
            "per": messageFormatted[9].split(": ")[1],
            "wis": messageFormatted[10].split(": ")[1],
        },
        "background": background,
        "imageUrl": generateImage(background)
    }
