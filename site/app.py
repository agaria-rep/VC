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
        return render_template("/profile/auth.html")

@app.route("/profile/auth", methods=['GET'])
def profile_auth():
    session["user_id"] = request.args.get("uid")
    session["name"] = request.args.get("first_name")
    session["last_name"] = request.args.get("last_name")
    session["photo"] = request.args.get("photo")

    return redirect("/profile")

if __name__ == "__main__":
    app.run(debug=True)