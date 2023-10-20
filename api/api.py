from dotenv import load_dotenv
from prompt import buildMessage
load_dotenv()

import os

import requests as req
import  json

headers = {"Authorization": f"Bearer {os.environ['OPENAI_TOKEN']}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
model_id = "gpt-3.5-turbo"

def generateImage(text, objectName):
    endpoint = "https://api.openai.com/v1/images/generations"
    resolution = "256x256"

    prompt = text if text else objectName
    
    message_body = {
        "prompt": prompt,
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
        "name": messageFormatted[0].split(": ")[1] if messageFormatted[0] else None,
        "alignment": messageFormatted[1].split(": ")[1] if messageFormatted[1] else None,
        "class": messageFormatted[2].split(": ")[1] if messageFormatted[2] else None,
        "race": messageFormatted[3].split(": ")[1] if messageFormatted[3] else None,
        "skill": messageFormatted[4].split(": ")[1] if messageFormatted[4] else None,
        "weapon": messageFormatted[11].split(": ")[1] if messageFormatted[11] else None,
        "attributes": {
            "hp": messageFormatted[5].split(": ")[1] if messageFormatted[5] else None, 
            "str": messageFormatted[6].split(": ")[1] if messageFormatted[6] else None,
            "dex": messageFormatted[7].split(": ")[1] if messageFormatted[7] else None,
            "car": messageFormatted[8].split(": ")[1] if messageFormatted[8] else None,
            "per": messageFormatted[9].split(": ")[1] if messageFormatted[9] else None,
            "wis": messageFormatted[10].split(": ")[1] if messageFormatted[10] else None,
        },
        "background": background,
        "imageUrl": generateImage(background, objectName)
    }
