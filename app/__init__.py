from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

file_path = os.path.abspath(os.getcwd())+"/movies.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
CORS(app)
db = SQLAlchemy(app)

from app import routes