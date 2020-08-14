from . import db
import datetime
from sqlalchemy import Column, DateTime, Integer, String


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, nullable=False,
                primary_key=True, autoincrement=True)
    hashed_password = Column(String, nullable=False)

    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    profile = Column(String, nullable=False)
    created_at = Column(
        DateTime, default=datetime.datetime.utcnow, nullable=False)
