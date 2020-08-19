import os

BASE_DIR = os.path.dirname(__file__)


class Config:
    PORT = 5000
    HOST = "0.0.0.0"
    JWT_SECRET_KEY = "1234"


class DevelopmentConfig(Config):
    DEBUG = True

    SQLITE_PATH = os.getenv('SQLITE_PATH', None)
    if SQLITE_PATH:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + SQLITE_PATH
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
            os.path.join(BASE_DIR, 'db/dev.db'))
    # uwsgi 로 실행할때 절대 경로로 줘야함 (////)
    # Docker 로 Nginx 실행할때 아래 코드 사용
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////www/db/dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    print("====================CONFIG====================")
    print(SQLALCHEMY_DATABASE_URI)
    print("==============================================")


class ProductionConfig(Config):
    DEBUG = False


class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
        os.path.join(BASE_DIR, 'db/test.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig,
    test=TestConfig
)
