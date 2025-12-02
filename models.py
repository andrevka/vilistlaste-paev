import sqlite3
from flask_sqlalchemy import SQLAlchemy

connection = sqlite3.connect(":memory:", check_same_thread=False)

def create_sqlite_connection():
    return connection;

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
