import pytest
from project import create_app
from project.models import db


@pytest.fixture(scope='session')
def app():
    app = create_app('test')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()
