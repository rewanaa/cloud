import flask
from flask_restful import Resource, request
from .model import conn
from .token_generator import hash_password

class User(Resource):
    def __init__(self):
        super().__init__()

    def post(self):
        """
        Expected parameters
        first_name
        last_name
        email
        password
        """
        user = request.get_json(force=True)
        conn.execute('''INSERT INTO user(user_first_name, user_last_name, email, password) VALUES(?,?,?,?)''',
                     (user['first_name'],
                      user['last_name'],
                      user['email'],
                      hash_password(user['password'])))
        conn.commit()
        return {'message': 'User Added Successfully'}, 200
