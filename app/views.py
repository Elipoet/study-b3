from app import app

from flask import render_template, flash

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

# Création Formulaire Connexion
class ConnexionForm(FlaskForm):
    name = StringField("Nom Utilisateur", validators=[DataRequired()])
    submit = SubmitField("Soumettre")

# Page Connexion
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    name = None
    form = ConnexionForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data= ''
        # flash("Connexion réussie")

    return render_template("public/connexion.html",
                           name = name,
                           form = form
                           )