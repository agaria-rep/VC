from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
import requests
import os

try:
    import secret
    print('Running on local\n\n')
    secret.setValues()
except ImportError or ModuleNotFoundError:
    print('Running on server\n\n')

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
    if not "user_id" in session:
        session["user_id"] = "Неизвестно"
        session["name"] = "Неизвестный"
        session["last_name"] = "по фамилии Неизвестный"
        session["photo"] = "/static/images/profile/standart_photo.png"

    return render_template("/profile/index.html", user_id=session["user_id"], first_name=session["name"], last_name=session["last_name"], photo=session["photo"])

@app.route("/profile/auth", methods=['GET'])
def profile_auth():
    return render_template("/profile/auth.html")

@app.route("/profile/login", methods=['GET'])
def profile_login():
    session["user_id"] = request.args.get("uid")
    session["name"] = request.args.get("first_name")
    session["last_name"] = request.args.get("last_name")
    session["photo"] = request.args.get("photo_rec")

    return redirect("/profile")

@app.route("/profile/logout")
def profile_logout():
    session["user_id"] = "Неизвестно"
    session["name"] = "Неизвестный"
    session["last_name"] = "по фамилии Неизвестный"
    session["photo"] = "/static/images/profile/standart_photo.png"

    return redirect("/profile")

if __name__ == "__main__":
    app.run()