from . import db


class Post(db.Model):
    id = db.Column(db.Integer, nullable=False,
                   primary_key=True, autoincrement=True)

    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text())
    create_date = db.Column(db.DateTime(), nullable=False)
