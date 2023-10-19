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

    background = messageFormatted[8].split("BKG: ")[1]

    return {
        "name": messageFormatted[0].split("NAME: ")[1],
        "class": messageFormatted[1].split("CLASS: ")[1],
        "attributes": {
            "hp": messageFormatted[2].split("HP: ")[1], 
            "str": messageFormatted[3].split("STR: ")[1],
            "dex": messageFormatted[4].split("DEX: ")[1],
            "car": messageFormatted[5].split("CAR: ")[1],
            "per": messageFormatted[6].split("PER: ")[1],
            "wis": messageFormatted[7].split("WIS: ")[1],
        },
        "background": background,
        "imageUrl": generateImage(background)
    }
