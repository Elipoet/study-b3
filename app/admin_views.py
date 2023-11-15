from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask import render_template, flash

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

# Nouveau MySQL db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Users'
app.config['SECRET_KEY'] = "secret_key_studi"
# Ancien MySQL db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Création Formulaire Utilisateurs
class UserForm(FlaskForm):
    name = StringField("Nom", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Mot de Passe", validators=[DataRequired()])
    submit = SubmitField("Soumettre")

# Création modèle
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name

@app.route("/admin/ajout-utilisateur", methods=['GET', 'POST'])
def ajout_utilisateur():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        form.password.data = ''
        # flash("Utilisateur ajouté")
    our_users = Users.query.order_by(Users.date_added)
    return render_template("admin/ajout-utilisateur.html",
                           form=form,
                           name=name,
                           our_users=our_users)

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

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route("/admin/profile")
def admin_profile():
    return render_template("admin/profile.html")
