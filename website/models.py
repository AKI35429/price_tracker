from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(10000))
    large_url = db.Column(db.String(100000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    req_price = db.Column(db.Integer)
    curr_price = db.Column(db.Integer)
    short_url = db.Column(db.String(1000))  # Store the short URL
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
