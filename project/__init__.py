from flask import Flask
from config import config_by_name


def create_app(env='dev'):
    app = Flask(__name__)

    # Configure
    app.config.from_object(config_by_name[env])

    # BluePrints
    from . import models, routes
    routes.init_app(app)
    models.init_app(app)

    return app
