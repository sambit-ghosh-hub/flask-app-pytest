import sys
sys.path.insert(0, 'D:\All\Dev\devops\maincourse\class13\flask-hello-world')

import pytest
from app import app as flask_app
@pytest.fixture
def app():
    yield flask_app
@pytest.fixture
def client(app):
    return app.test_client()
