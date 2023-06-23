from flask import Flask, request, render_template, redirect, url_for, make_response

app = Flask(__name__)

@app.route("/")
def index():
    lang = request.cookies.get('lang')
    if lang == None:
        return redirect("/lang/ru/")
    else:
        return render_template("./"+lang+"/index.html")

@app.route("/lang/<name>/")
def lang(name):
    response = make_response(redirect("/"))
    response.set_cookie("lang", name)
    
    return response

app.run(debug=True)