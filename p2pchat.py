from datetime import datetime
from flask import Blueprint, render_template, session
from flask_socketio import send

br = Blueprint("chat", __name__)

@br.route("/p2p-chat-user-list")
def sockets():
    return render_template("application/p2p-chat-user-list.html", year=datetime.now().year)


def register_socketio_handlers(socketio):

    @socketio.on("message")
    def handle_message(msg):
        print(msg)
