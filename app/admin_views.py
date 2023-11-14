from app import app

from flask import render_template, flash

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route("/admin/profile")
def admin_profile():
    return render_template("admin/profile.html")

# Création Formulaire
class ConnexionForm(FlaskForm):
    name = StringField("Nom Utilisateur", validators=[DataRequired()])
    submit = SubmitField("Soumettre")

# Page Connexion
@app.route('/admin-connexion', methods=['GET', 'POST'])
def admin_connexion():
    name = None
    form = ConnexionForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data= ''
        # flash("Connexion réussie")

    return render_template("admin/admin-connexion.html",
                           name = name,
                           form = form
                           )
