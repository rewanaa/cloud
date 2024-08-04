from flask import Blueprint
from ..forms import LoginForm
from flask_login import login_required, login_user, logout_user
from ..model import User
from flask import redirect, render_template, url_for, flash, request, Blueprint

accounts_bp = Blueprint("accounts", __name__)


@accounts_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    # Validate username and password (not shown here)
    if form.validate_on_submit():
        token = User.create_user_token(form.email.data, form.password.data)
        if token is None:
            return {'message': "unauthorized"}, 401
        else:
            login_user(User(token))
            # response = jsonify({'token': token})
            # response.set_cookie('access_token', token, httponly=True, secure=True)  # Secure cookie
            return redirect(url_for("core.home"))
    else:
        flash("Invalid email and/or password.", "danger")
        return render_template("accounts/login.html", form=form)


@accounts_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("accounts.login"))
