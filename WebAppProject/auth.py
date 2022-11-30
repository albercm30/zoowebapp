from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db, bcrypt
import flask_login
from flask_login import current_user
from . import model

bp = Blueprint("auth", __name__)

# Get par default
@bp.route("/signup")
def signup():
    return render_template("auth/signup.html")


@bp.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    # Check that passwords are equal
    if password != request.form.get("password_repeat"):
        flash("Sorry, passwords are different")
        return redirect(url_for("auth.signup"))
    # Check if the email is already at the database
    user = model.User.query.filter_by(email=email).first()
    if user:
        flash("Sorry, the email you provided is already registered")
        return redirect(url_for("auth.signup"))
    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = model.User(email=email, name=username, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    flash("You've successfully signed up!")
    return redirect(url_for("auth.login"))

@bp.route("/login")
def login():
    return render_template("auth/login.html")


@bp.route("/login", methods=["POST"])
def login_post():
    # Complete the following two lines:
    email = request.form.get("email")
    password = request.form.get("password")
    # Get the user with that email from the database:
    user = model.User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        # The user exists and the password is correct
        flask_login.login_user(user)
        return redirect(url_for("main.index"))
    else:
        # Wrong email and/or password
        # Complete this code to flash a message and redirect to the login form
        flash("Sorry, the email or the password is incorect")
        return redirect(url_for("auth.login"))


@bp.route("/logout", methods=["POST"])
def logout_post():
    flask_login.logout_user()
    return redirect(url_for("auth.login"))
