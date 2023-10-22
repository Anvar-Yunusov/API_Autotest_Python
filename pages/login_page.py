import requests

from utils.config import YANDEX_PASSPORT_API_URL


class LoginPage:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):

        response = requests.post(YANDEX_PASSPORT_API_URL + "/auth", data={
            "login": self.email,
            "password": self.password
        })
        return response
