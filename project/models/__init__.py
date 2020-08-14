from .base import db
from flask_migrate import Migrate


def init_app(app):
    print("INIT: DATABASE")
    db.init_app(app)
    # add new models here
    from . import users, posts
    migrate = Migrate()
    migrate.init_app(app, db)
