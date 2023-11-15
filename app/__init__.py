from flask import Flask

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import views
from app import admin_views

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key_studi"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Users'
db = SQLAlchemy(app)

