from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key_studi"

from app import views
from app import admin_views


