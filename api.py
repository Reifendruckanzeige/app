# dei uma pesquisada e a base da api fica +/- assim.
# precisamos criar uma conta nova para poder usar o free tier da open ai (o meu free tier expirou)
# ainda precisamos detalhar a api da maneira que precisamos para o projeto

from dotenv import load_dotenv
from prompt import BASE_MESSAGE
load_dotenv()

import os

import requests as req
import  json

headers = {"Authorization": f"Bearer {os.environ['OPENAI_TOKEN']}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
model_id = "gpt-3.5-turbo"

message_body = {
    "model": model_id,
    "messages": [{"role": "user", "content": BASE_MESSAGE}] 
}
message_body = json.dumps(message_body)

def ask():
    request = req.post(link, headers=headers, data=message_body)
    print(request)

    ans = request.json()
    print(ans)

    message = ans["choices"][0]["message"]["content"]
    return message
