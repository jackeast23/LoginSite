from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</>"

@auth.route('/logout')
def logout():
    return "<p>Logout</>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</>"