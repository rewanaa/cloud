from src.custom_login_manager import CustomLoginManager
from flask import abort, redirect, url_for, Flask
from flask_login import logout_user
from src import GLOBAL
from src.model import User
from src.core.views import core_bp
from src.api import api_bp
from src.accounts import accounts_bp

app = Flask(__name__, static_url_path='', static_folder='./src/static', template_folder='./src/templates')
app.secret_key = GLOBAL.SECRET_KEY

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
app.register_blueprint(api_bp)

login_manager = CustomLoginManager()
login_manager.login_view = "accounts.login"
login_manager.login_message_category = "danger"
login_manager.init_app(app)


@login_manager.user_loader
def refresh_login(user_token):
    user = User(user_token)
    if not login_manager.validate_token(user):
        return None
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    logout_user()
    return redirect(url_for("accounts.login"))

@app.errorhandler(401)
def unauthorized(error):
    response = abort(401)
    response.headers['WWW-Authenticate'] = 'Basic realm="Login Required"'  # Example header
    return response


if __name__ == '__main__':
    app.run(debug=True, host=GLOBAL.HOST, port=GLOBAL.PORT)
