from forms import UserLoginForm
from models import User, db, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash

# imports for flask login 
from flask_login import login_user, logout_user, LoginManager, current_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signin')
def sign_in():
    return render_template('sign_in.html')

@auth.route('/signup')
def sign_up():
    return render_template('sign_up.html')