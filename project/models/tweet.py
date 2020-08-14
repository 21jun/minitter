from sqlalchemy.sql.operators import nullslast_op
from . import db
import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey


class Tweet(db.Model):
    __tablename__ = 'tweet'

    id = Column(Integer, nullable=False,
                primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    text = Column(String, nullable=False)
    created_at = Column(
        DateTime, default=datetime.datetime.utcnow, nullable=False)
