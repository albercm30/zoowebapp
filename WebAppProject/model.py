from . import db
import flask_login


class User(flask_login.UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_manager = db.Column(db.Boolean, nullable=False, default=False)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.VARCHAR(500),  nullable=False)
    activities = db.relationship('Activity', backref='animal', lazy=True)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False, unique=True)
    description = db.Column(db.VARCHAR(500), nullable=False)
    minimum_age = db.Column(db.Integer, default=3)
    is_marked = db.Column(db.Boolean, nullable=False, default=False)

class Scheduledactivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    stating_time = db.Column(db.Time(), nullable=False)
    duration = db.Column(db.Integer,  nullable=False)
    places = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('scheduledactivity.id'), nullable=False)
    places = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(), nullable=False)



