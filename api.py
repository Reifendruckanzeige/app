from dotenv import load_dotenv
from prompt import buildMessage
load_dotenv()

import os

import requests as req
import  json

headers = {"Authorization": f"Bearer {os.environ['OPENAI_TOKEN']}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
model_id = "gpt-3.5-turbo"

def acessGPT(objectName):
    message = {
        "character": {
            "name": "Carlos, o Valente",
            "class": "Guerreiro",
            "region": "Artalúdico",
        },
        "attrs": {
            "hp": "100", # pontos de vida
            "str": "10", # forca
            "dex": "10", # destreza
            "car": "10", # carisma
            "per": "10", # percepcao
            "wis": "10", # inteligencia/sabedoria
            "con": "10", # constituicao
        },
        "background": "Carlos, o Valente, e um Guerreiro habil com espada longa e preciso nos seus tiros de arco e flecha"
    }
    # message_body = {
    #     "model": model_id,
    #     "messages": [{"role": "user", "content": buildMessage(objectName)}] 
    # }
    # message_body = json.dumps(message_body)

    # request = req.post(link, headers=headers, data=message_body)
    # ans = request.json()

    # message = ans["choices"][0]["message"]["content"]
    return message
