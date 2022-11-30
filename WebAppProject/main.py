import datetime
import dateutil.tz
import flask_login
from flask_login import current_user
from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db, bcrypt


from . import model

bp = Blueprint("main", __name__)

@bp.route("/")
# @flask_login.login_required
def index():
    return render_template("main/index.html")

@bp.route("/animals")
# @flask_login.login_required
def animals():
    return render_template("main/animal.html")

@bp.route("/customer")
# @flask_login.login_required
def customers():
    return render_template("main/customer.html")

@bp.route("/activity")
# @flask_login.login_required
def activities():
    return render_template("main/activity.html")