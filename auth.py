from datetime import datetime
from flask import Blueprint, redirect, render_template, request, session, url_for

from models import User, db

br = Blueprint("auth", __name__)


@br.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            error = "Invalid username or password"
            return render_template("login.html", error=error)

    # GET → show the form
    return render_template("login.html")


@br.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        password = request.form.get("password", "")
        email = request.form.get("email", "").strip().lower()
        confirm = request.form.get("confirm", "")

        # Validation
        if not username or not password:
            return render_template("signup.html", error="Please fill in all fields.")

        if password != confirm:
            return render_template("signup.html", error="Passwords do not match.")

        if User.query.filter_by(username=username).first():
            return render_template("signup.html", error="Username already taken.")

        db.session.add(User(username=username, password=password, email=email))
        db.session.commit()

        session["username"] = username

        return redirect(url_for("home"))

    return render_template("signup.html", year=datetime.now().year)


@br.route("/logout")
def logout():
    session.pop("username", None)  # remove from session if exists
    return redirect(url_for("home"))
