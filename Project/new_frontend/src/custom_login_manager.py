from flask_login import LoginManager
import requests
from .GLOBAL import IDENTITY_SERVER
from flask import abort


class CustomLoginManager(LoginManager):

    def validate_token(self, user):
        response = requests.post(IDENTITY_SERVER + "/validate", json={"token": user.token})
        if response.status_code == 200:
            return True
        else:
            return False



