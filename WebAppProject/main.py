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
    activities = model.Activity.query.order_by(model.Activity.id.desc()).all()
    cheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()
    return render_template("main/activity.html",activities=activities, cheduleds=cheduleds)

@bp.route("/activity/",methods=["POST"])
@flask_login.login_required
def add_activity():
    title = request.form.get("title")
    minimum_age = request.form.get("minimum_age")
    description = request.form.get("description")
    new_activity = model.Activity(title=title, description=description, minimum_age=minimum_age,is_marked=False)
    db.session.add(new_activity)
    db.session.commit()
    flash("You've successfully added an activity")
    activities = model.Activity.query.order_by(model.Activity.id.desc()).all()
    cheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()
    return render_template("main/activity.html",activities=activities, cheduleds=cheduleds)

@bp.route("/activitysched",methods=["POST"])
@flask_login.login_required
def add_schedule():
    # activity_title, date, starting_time,duration, places, price  
    activity_title = request.form.get("activity_title")
    activity = model.Activity.query.filter_by(title=activity_title).first()
    activity_id = activity.id
    date = request.form.get("date")
    starting_time = request.form.get("starting_time")
    duration = request.form.get("duration")
    places = request.form.get("places")
    price = request.form.get("price")
    new_schedule= model.Scheduledactivity(activity_id=activity_id, date=date, stating_time=starting_time,
    duration=duration, places=places, price=price)
    db.session.add(new_schedule)
    db.session.commit()
    flash("You've successfully added scheduled the activityy")
    activities = model.Activity.query.order_by(model.Activity.id.desc()).all()
    cheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()
    return render_template("main/activity.html",activities=activities, cheduleds=cheduleds)

    
@bp.route("/activitymark",methods=["POST"])
@flask_login.login_required
def mark_activity():
    # activity_title, date, starting_time,duration, places, price  
    activity_title = request.form.get("activity_title")
    activity = model.Activity.query.filter_by(title=activity_title).first()
    is_it_marked = request.form.get("is_it_marked")
    if is_it_marked == "Yes":
        is_it_marked = True
    else :
        is_it_marked = False
    setattr(activity, 'is_marked', is_it_marked)
    db.session.commit()
    flash("You've successfully added scheduled the activityy")
    activities = model.Activity.query.order_by(model.Activity.id.desc()).all()
    cheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()
    return render_template("main/activity.html",activities=activities, cheduleds=cheduleds)