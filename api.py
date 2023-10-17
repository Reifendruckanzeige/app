# dei uma pesquisada e a base da api fica +/- assim.
# precisamos criar uma conta nova para poder usar o free tier da open ai (o meu free tier expirou)
# ainda precisamos detalhar a api da maneira que precisamos para o projeto

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
    # rpgContent = {
    #     'character': f"Personagem {objectName}",
    #     'attrs': 'Atributos',
    #     'background': 'Historia generica de background'
    # }
    message_body = {
        "model": model_id,
        "messages": [{"role": "user", "content": buildMessage(objectName)}] 
    }
    message_body = json.dumps(message_body)

    request = req.post(link, headers=headers, data=message_body)
    ans = request.json()

    message = ans["choices"][0]["message"]["content"]
    # return rpgContent
    return message
