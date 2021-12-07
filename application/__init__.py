from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import closerange, getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")

db = SQLAlchemy(app)

from application import routes
