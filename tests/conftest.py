from fastapi.testclient import TestClient
import pytest

from app.main import app
from app.config.app_settings import AppSettings, get_settings

def get_settings_override():
    return AppSettings(url_one='https://test_one.com')


@pytest.fixture(scope='module')
def client_app():
    with TestClient(app) as client:
        app.dependency_overrides[get_settings] = get_settings_override
        yield client
