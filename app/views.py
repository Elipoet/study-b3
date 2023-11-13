from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/public/a-propos")
def public_a_propos():
    return render_template("public/a-propos.html")