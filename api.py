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

    # request = req.post(endpoint, headers=headers, data=message_body)
    # ans = request.json()

    # return ans["data"][0]["url"]

    # REMOVER ESSE EXEMPLO
    return "https://oaidalleapiprodscus.blob.core.windows.net/private/org-gRhYSBVepOCJW4eWQhzEHSE7/user-NYnrVKKYj5ZRM6fDxPIhjJ5o/img-rnm6CArab48mkuAnKs8u9m2a.png?st=2023-10-19T03%3A29%3A38Z&se=2023-10-19T05%3A29%3A38Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-10-18T19%3A43%3A33Z&ske=2023-10-19T19%3A43%3A33Z&sks=b&skv=2021-08-06&sig=AMcSm%2B52rq0Dy94bMcvi2cmw2Btihx/po9c%2BKkY6ebM%3D"

def accessGPT(objectName, charLevel):
    # message_body = {
    #     "model": model_id,
    #     "messages": [{"role": "user", "content": buildMessage(objectName, charLevel)}] 
    # }
    # message_body = json.dumps(message_body)

    # request = req.post(link, headers=headers, data=message_body)
    # ans = request.json()

    # data = ans["choices"][0]["message"]["content"]
    
    # REMOVER ESSE EXEMPLO
    data = "NAME: Cedric, o Sólido/CLASS: Guerreiro/HP: 28/STR: 8/DEX: 5/CAR: 6/PER: 6/WIS: 5/BKG: Cedric, o Sólido, nasceu em uma pequena vila às margens de uma floresta encantada. Desde jovem, ele demonstrava uma força incomum, capaz de erguer objetos pesados com facilidade. Sua devoção à vila o levou a treinar incansavelmente nas artes da guerra, tornando-se um guerreiro habilidoso e respeitado. Apesar de sua imponente presença, Cedric é conhecido por sua gentileza e capacidade de liderança. Ele é um defensor dedicado de seu povo, e sua determinação em proteger sua terra natal é inabalável. Em uma jornada para desvendar os mistérios da floresta encantada, Cedric busca fortalecer ainda mais suas habilidades e encontrar aliados que compartilhem de sua causa."
    
    messageFormatted = data.split("/")

    imageUrl = generateImage(data)
    
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
        "background": messageFormatted[8].split("BKG: ")[1],
        "imageUrl": imageUrl
    }