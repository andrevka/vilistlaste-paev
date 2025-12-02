from datetime import datetime
from flask import Blueprint, render_template, session
from flask_socketio import send

br = Blueprint("chat", __name__)


@br.route("/sockets")
def sockets():
    return render_template("sockets.html", year=datetime.now().year)


def register_socketio_handlers(socketio):

    @socketio.on("message")
    def handle_message(msg):
        print("Received message:", msg)
        send(
            {
                **msg,
                "username": session.get("username", "Anonymous"),
                "session_id": session.get("session_id", None),
            },
            broadcast=True,
        )
