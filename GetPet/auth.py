from flask import Blueprint, render_template, request, flash, redirect, url_for
#from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
#from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/registeruser',methods=['GET','POST'])
def registeruser():
    return render_template("registeruser.html")

@auth.route('/reg_asos',methods=['GET','POST'])
def reg_asos():
    return render_template("reg_asos.html")

@auth.route('/registerbussines',methods=['GET','POST'])
def registerbussines():
    return render_template("registerbussines.html")

@auth.route('/register',methods=['GET','POST'])
def register():
    return render_template("register.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    pass