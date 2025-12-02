from datetime import datetime
from flask import Blueprint, render_template, session
from flask_socketio import send

br = Blueprint("p2pchat", __name__)

@br.route("/p2p-chat-user-list")
def userlist():
    return render_template("application/p2p-chat-user-list.html", year=datetime.now().year)

@br.route("/p2p-chat/<peer>")
def chat(peer):
    return render_template("application/p2p-chat.html", year=datetime.now().year)


def register_socketio_handlers(socketio):

    @socketio.on("message")
    def handle_message(msg):
        print(msg)
