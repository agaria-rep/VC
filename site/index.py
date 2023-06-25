from flask import Flask, request, render_template, redirect, url_for, make_response
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/map")
def map():
    return render_template("/map/index.html")

@app.route("/map/load")
def map_load():
    return requests.get("https://oovc.piwerm.repl.co/map")