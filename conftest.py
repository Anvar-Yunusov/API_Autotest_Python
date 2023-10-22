import pytest
import requests

from pages.login_page import LoginPage
from utils.config import EMAIL, PASSWORD, TOKEN, LOGOUT_URL


@pytest.fixture
def login_and_get_token():
    login_page = LoginPage(EMAIL, PASSWORD)
    response = login_page.login()
    assert response.status_code == 200, "Ошибка авторизации аккаунта"
    yield TOKEN


@pytest.fixture
def logout(login_and_get_token):
    yield
    response = requests.get(LOGOUT_URL, headers={"Authorization": f"OAuth {login_and_get_token}"})
    assert response.status_code == 200, "Ошибка при попытки разлогиниться"
