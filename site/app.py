from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
import requests
import os

app = Flask(__name__)
app.secret_key = os.environ.get('secret_key')

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/map")
def map():
    return render_template("/map/index.html")

@app.route("/profile")
def profile():
    if "user_id" in session:
        return render_template("/profile/index.html", id=session["user_id"])
    else:
        return redirect("https://oauth.vk.com/authorize?client_id="+os.environ.get('api_key')+"&display=page&redirect_uri=https://oovg.vercel.app/code&scope=offline&response_type=code&v=5.131")

@app.route("/code", methods=['GET', 'POST'])
def auth_code():
    code = request.args.get("code")
    return redirect("https://oauth.vk.com/access_token?client_id="+os.environ.get('api_key')+"&client_secret="+os.environ.get('api_secret_key')+"&redirect_uri=http://oovg.vercel.app/token&code="+code)

@app.route("/token", methods=['GET', 'POST'])
def auth_token():
    session["user_id"] = request.get_json()["user_id"]
    return redirect("/profile")