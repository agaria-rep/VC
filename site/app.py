from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
import requests
import os

if __name__ == "__main__":
    os.environ.setdefault('secret_key', 'aboba')
    os.environ.setdefault('api_key', '51698534')
    os.environ.setdefault('api_secret_key', 'w0ENS8syb5rCbeUhbPPW')

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
        return render_template("/profile/auth.html")

@app.route("/profile/auth", methods=['GET'])
def profile_auth():
    return render_template("/profile/auth.html")

if __name__ == "__main__":
    app.run(debug=True)