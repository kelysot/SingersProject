from flask import Blueprint, render_template, request, redirect
from flask_bcrypt import Bcrypt
from services.user import login_service, register_service, logout_service

user_bp = Blueprint('user', __name__)
bcrypt = Bcrypt()


@user_bp.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        return register_service(username, email, password, confirm_password)
    else:
        return render_template('register.html')


@user_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return login_service(username, password)
    return render_template('login.html')


@user_bp.route('/logout')
def logout():
    return logout_service()



