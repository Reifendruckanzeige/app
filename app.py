from flask import Flask, redirect, render_template
from requests import request
from api import ask

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/setup", methods = ["GET"])
def setup():
    return render_template("setup.html")

@app.route("/send", methods = ["POST"])
def send():
    # Talvez aqui eu receba a string da funcao ask e jogue
    # para o endpoint do personagem

    message = ask()
    return redirect("/character")

@app.route("/character", methods = ["GET"])
def character():
    return render_template("character.html")
