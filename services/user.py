from flask import redirect, url_for, flash, session
from models import User
from database import db
from flask_jwt_extended import create_access_token
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()


def register_service(username, email, password, confirm_password):
    # Check if the length of username is shorter than 3.
    if len(username) < 3:
        flash('Username must be at least 3 characters long', 'error')
        return redirect(url_for('user.register'))

    # Check if the length of password is shorter than 8.
    if len(password) < 8:
        flash('Password must be at least 8 characters long', 'error')
        return redirect(url_for('user.register'))

    # Check if the passwords match
    if password != confirm_password:
        flash('Passwords do not match. Please try again.', 'danger')
        return redirect(url_for('user.register'))

    # Check if the username or email already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        flash('Username or email already exists. Please choose different credentials.', 'danger')
        return redirect(url_for('user.register'))

    # Hash the password before storing in the database
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    session['user_id'] = new_user.id

    return redirect(url_for('singer.show_singers'))


def login_service(username, password):
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        session['user_id'] = user.id
        return redirect(url_for('singer.show_singers'))
    else:
        flash('Login unsuccessful. Please check your username and password.', 'danger')
        return redirect(url_for('user.login'))


def logout_service():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('user.login'))


def get_user_by_id(user_id):
    return User.query.get(user_id)
