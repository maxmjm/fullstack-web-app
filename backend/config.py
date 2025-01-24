from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable cross-origin requests

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" # Specify location of local SQLite database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Do not track modifications to database

db = SQLAlchemy(app) # Create instance of database
