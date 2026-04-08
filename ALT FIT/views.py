from app import app
from flask import render_template, request, redirect, url_for
@app.route('/')
def homepage():
    return render_template("home.html")
@app.route ("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "ana" and senha == "123":
            return redirect(url_for("dashboard"))
        else:
            return "usuario ou senha incorretos"

    return render_template ("login.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")