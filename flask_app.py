from flask import Flask, render_template, session
from flask_socketio import SocketIO

from datetime import datetime
import uuid

from sqlalchemy import StaticPool

import instructions
from models import create_sqlite_connection, db

import hello
import auth
import chat
import sql


app = Flask(__name__)

app.secret_key = "a-very-secret-key"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "creator": create_sqlite_connection,
    "poolclass": StaticPool,
}

app.register_blueprint(hello.bp)
app.register_blueprint(auth.br)
app.register_blueprint(chat.br)
app.register_blueprint(instructions.bp)
app.register_blueprint(sql.bp)

socketio = SocketIO(app)

chat.register_socketio_handlers(socketio)

with app.app_context():
    db.init_app(app)
    db.create_all()


@app.before_request
def ensure_session_id():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())


@app.route("/")
def home():
    return render_template("index.html", year=datetime.now().year)


@app.route("/content")
def content():
    return render_template("content.html", year=datetime.now().year)


if __name__ == "__main__":
    socketio.run(app=app, debug=True, host="0.0.0.0", port=8080)
