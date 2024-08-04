from datetime import datetime, timedelta
from flask_login import UserMixin
from .GLOBAL import IDENTITY_SERVER
import requests


class User(UserMixin):
    def __init__(self, token):
        self.token = token

    def get_id(self):
        return self.token

    @staticmethod
    def create_user_token(email, password):
        response = requests.post(IDENTITY_SERVER + "/login", json={"password": password, "email": email})
        if response.status_code == 200:
            return response.json()['token']
        else:
            return None
