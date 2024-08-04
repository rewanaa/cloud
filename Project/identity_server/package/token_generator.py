import hashlib
import secrets


def generate_token(length=64):
    return secrets.token_urlsafe(length)


def hash_password(password:str):
    return hashlib.sha512(password.encode('utf-8')).hexdigest()