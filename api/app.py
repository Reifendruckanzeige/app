from flask import Flask, redirect, render_template, request
from api import accessGPT

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
        charLevel = request.form.get("charLevel")
        
        if(objectName and charLevel):
            character = accessGPT(objectName, charLevel)
            return render_template("character.html", character=character, objectName=objectName, charLevel=charLevel)
        
        errors = {
            "message": "Houve erro ao ler o campos do formulário!"
        }

        return render_template("setup.html", errors=errors)
    return redirect("/")
