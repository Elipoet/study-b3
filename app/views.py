from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/public/a-propos")
def public_a_propos():
    return render_template("public/a-propos.html")

# Page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_pages/404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("error_pages/404.html"), 500