# dei uma pesquisada e a base da api fica +/- assim.
# precisamos criar uma conta nova para poder usar o free tier da open ai (o meu free tier expirou)
# ainda precisamos detalhar a api da maneira que precisamos para o projeto

from key import API_KEY # essa API_KEY vem de outro arquivo que contem somente a chave
import requests as req
import  json

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

body_mensagem = {
    "model": id_modelo,
    "messages": [{"role": "user", "content": "Escreva o hino oficial do maior time do mundo (palmeiras)"}] 
}
body_mensagem = json.dumps(body_mensagem)

requisicao = req.post(link, headers=headers, data=body_mensagem)
print(requisicao)

resposta = requisicao.json()
print(resposta)

mensagem = resposta["choices"][0]["message"]["content"]
print(mensagem)
