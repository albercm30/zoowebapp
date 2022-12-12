import datetime
import dateutil.tz
import flask_login
from flask_login import current_user
from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db, bcrypt
from datetime import datetime


from . import model

bp = Blueprint("main", __name__)

@bp.route("/")
# @flask_login.login_required
def index():
    activities = model.Activity.query.order_by(model.Activity.id.desc()).all()
    scheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()
    return render_template("main/index.html",activities=activities,scheduleds=scheduleds)

@bp.route("/animals")
# @flask_login.login_required
def animals():
    return render_template("main/animal.html")

@bp.route("/customer")
@flask_login.login_required
def customers():
    activities = model.Activity.query.order_by(model.Activity.id.desc()).all()
    scheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()
    # for each activity title let's associate all of its available dates from the scheduled activities
    act_dates ={}
    #Same but with id of the activity as a key
    act_id = {}   
    for activity in activities:
        for scheduled in scheduleds:
            if activity.id == scheduled.activity_id:
                if activity.is_marked:
                    act_dates[activity.title]=[] 
                    act_id[activity.title]=[] 

    for activity in activities:
        for scheduled in scheduleds:
            if activity.id == scheduled.activity_id:
                if activity.is_marked:
                    act_dates[activity.title].append(scheduled.date)
                    act_id[activity.title]= activity.id
    return render_template("main/customer.html",activities=activities,scheduleds=scheduleds,act_dates=act_dates,act_id=act_id)

@bp.route("/customer",methods=["POST"])
@flask_login.login_required
def booking():
    activities = model.Activity.query.order_by(model.Activity.id.desc()).all()
    scheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()

    # for each activity title let's associate all of its available dates from the scheduled activities
    act_dates ={}
    #Same but with id of the activity as a key
    act_id = {}   
    for activity in activities:
        for scheduled in scheduleds:
            if activity.id == scheduled.activity_id:
                if activity.is_marked:
                    act_dates[activity.title]=[] 
                    act_id[activity.title]=[] 

    for activity in activities:
        for scheduled in scheduleds:
            if activity.id == scheduled.activity_id:
                if activity.is_marked:
                    act_dates[activity.title].append(scheduled.date)
                    act_id[activity.title]= activity.id
    
    activity_title_booked = request.form.get("activity_title_booked")
    scheduled_date = request.form.get("date_chosen")
    activity = model.Activity.query.filter_by(title=activity_title_booked).first()
    activity_id = activity.id
    print("scheduled_date",type(scheduled_date))
    scheduled = model.Scheduledactivity.query.filter_by(activity_id=activity_id,date=scheduled_date).first()
    places_booked = request.form.get("places_booked")
    places_booked = int(places_booked)
    print(activity_title_booked,scheduled_date,places_booked)
    date_time = datetime.now(dateutil.tz.tzlocal())
    
    if places_booked > scheduled.places:
        flash("There not enough available places")
    else :
        new_reservation = model.Reservation(user_id=current_user.id,activity_id=scheduled.activity_id,places=places_booked,
        date=date_time)
        db.session.add(new_reservation)
        setattr(scheduled, 'places', scheduled.places - places_booked)
        db.session.commit()
        flash("Your reservation is successful")
    return render_template("main/customer.html",activities=activities,act_dates=act_dates,scheduleds=scheduleds,act_id=act_id)

@bp.route("/activity")
# @flask_login.login_required
def activities():
    activities = model.Activity.query.order_by(model.Activity.id.desc()).all()
    scheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()
    return render_template("main/activity.html",activities=activities, scheduleds=scheduleds)

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
    scheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()
    return render_template("main/activity.html",activities=activities, scheduleds=scheduleds)

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
    #verify that  the activity isn't already schedule for this date 
    activities = model.Activity.query.order_by(model.Activity.id.desc()).all()
    scheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()
    for schedule in scheduleds:
        if str(schedule.date) == str(new_schedule.date):  
            if schedule.activity_id == new_schedule.activity_id:
                flash("This activity was already scheduled that day")
                return render_template("main/activity.html",activities=activities, scheduleds=scheduleds)
            
    db.session.add(new_schedule)
    db.session.commit()
    flash("You've successfully added scheduled the activityy")
    activities = model.Activity.query.order_by(model.Activity.id.desc()).all()
    scheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()
    return render_template("main/activity.html",activities=activities, scheduleds=scheduleds)

    
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
    scheduleds = model.Scheduledactivity.query.order_by(model.Scheduledactivity.id.desc()).all()
    return render_template("main/activity.html",activities=activities, scheduleds=scheduleds)