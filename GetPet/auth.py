from flask import Flask, Blueprint, app, render_template, request, flash, redirect, url_for, send_from_directory
import sqlalchemy
from .models import User, BusinessUser,AssociationUser
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user,login_manager
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/registeruser',methods=['GET','POST'])
def registeruser():
    email = request.form.get('email')
    password1 = request.form.get('psw')
    password2 = request.form.get('psw-repeat')
    user1 = User.query.filter_by(email=email).first()
    user2 = BusinessUser.query.filter_by(email=email).first()
    user3 = AssociationUser.query.filter_by(email=email).first()
    if user1 or user2 or user3:
        return render_template("registeruser.html", exists=True)
        # user exists
    elif password1!=password2:
        flag=False
        return render_template("register.html")

    if request.method == 'POST' and email and password1:
        new_user = User(email=email, password=password1)
        db.session.add(new_user)
        db.session.commit()

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