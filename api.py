from dotenv import load_dotenv
from prompt import buildMessage
load_dotenv()

import os

import requests as req
import  json

headers = {"Authorization": f"Bearer {os.environ['OPENAI_TOKEN']}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
model_id = "gpt-3.5-turbo"

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
    data = "NAME: Theron, CLASS: Arqueiro, HP: 15, STR: 1, DEX: 4, CAR: 2, PER: 3, WIS: 0, BKG: Theron, um hábil arqueiro, nasceu nas vastas florestas de Eldorin, onde aprendeu a arte da caça e a habilidade de se mover silenciosamente entre as árvores. Sua força física pode não ser impressionante, mas sua destreza e agilidade são incomparáveis. Com um olhar perspicaz, ele percebe os detalhes mais sutis na natureza ao seu redor, tornando-se um rastreador exímio. Embora não seja o mais carismático, sua presença tranquila e serena é reconfortante para aqueles ao seu redor. Theron nunca foi inclinado para os caminhos da magia, preferindo confiar em sua habilidade com o arco e flecha. Sua vida é dedicada a proteger as florestas e as criaturas que nelas habitam, tornando-se um guardião incansável da natureza."
    messageFormatted = data.split(",")
    
    return {
        "character": {
            "name": messageFormatted[0].split("NAME: ")[1],
            "class": messageFormatted[1].split("CLASS: ")[1],
        },
        "attrs": {
            "hp": messageFormatted[2].split("HP: ")[1], 
            "str": messageFormatted[3].split("STR: ")[1],
            "dex": messageFormatted[4].split("DEX: ")[1],
            "car": messageFormatted[5].split("CAR: ")[1],
            "per": messageFormatted[6].split("PER: ")[1],
            "wis": messageFormatted[7].split("WIS: ")[1],
        },
        "background": messageFormatted[8].split("BKG: ")[1]
    }