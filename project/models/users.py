from . import db
import datetime
from sqlalchemy import Column, DateTime, Integer


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, nullable=False,
                   primary_key=True, autoincrement=True)
    hashed_password = db.Column(db.String, nullable=False)

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    profile = db.Column(db.String, nullable=False)
