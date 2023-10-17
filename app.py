from flask import Flask, redirect, render_template, request
from api import acessGPT

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/setup", methods = ["GET"])
def setup():
    return render_template("setup.html", errors={"message":""})

@app.route("/send", methods = ["POST"])
def send():
    if request.method == "POST":
        objectName = request.form.get("objectName")
        
        if(objectName):
            # rpgContent = acessGPT(objectName)
            # return render_template("character.html", rpgContent=rpgContent)
            message = acessGPT(objectName)
            return render_template("character.html", message=message, objectName=objectName)
        
        errors = {
            "message": "Houve erro ao ler o nome do objeto escrito"
        }

        return render_template("setup.html", errors=errors)