from flask import Flask
from config import config_by_name


def creat_app():
    app = Flask(__name__)

    # Configure
    app.config.from_object(config_by_name["dev"])

    # BluePrints
    from . import models, routes
    routes.init_app(app)
    models.init_app(app)

    return app
