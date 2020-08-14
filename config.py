import os

BASE_DIR = os.path.dirname(__file__)


class Config:
    PORT = 5000
    HOST = "0.0.0.0"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
        os.path.join(BASE_DIR, 'db/test.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
