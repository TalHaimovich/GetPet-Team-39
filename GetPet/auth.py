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



@auth.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('css', path)


@auth.route('/images/<path:path>')
def serve_images(path):
    return send_from_directory('images', path)

@auth.route('/login',methods=['GET','POST'])
def login():
    email1 = request.form.get('email')
    password1 = request.form.get('psw')
    user1 = User.query.filter_by(email=email1).first()
    user2 = BusinessUser.query.filter_by(email=email1).first()
    user3= AssociationUser.query.filter_by(email=email1).first()
    if (user1 and user1.password == password1) or (user2 and user2.password == password1) or (user3 and user3.password==password1):
        return render_template("login.html")
    return render_template("index.html")

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

    email = request.form.get('email')
    password1 = request.form.get('psw')
    password2 = request.form.get('psw-repeat')
    name = request.form.get('name')
    adress = request.form.get('adress')
    user = BusinessUser.query.filter_by(email=email).first()
    user1 = User.query.filter_by(email=email).first()
    user2 = BusinessUser.query.filter_by(email=email).first()
    user3 = AssociationUser.query.filter_by(email=email).first()
    if user1 or user2 or user3:
        # user exists
        return render_template("reg_asos.html", exists=True)
    if password1!=password2:
        flag=False
        return render_template("register.html")


    if request.method == 'POST' and email and password1:
        new_user = AssociationUser(email=email, password=password1, name=name, adress=adress)
        db.session.add(new_user)
        db.session.commit()

    return render_template("reg_asos.html")

@auth.route('/registerbussines',methods=['GET','POST'])
def registerbussines():
    email = request.form.get('email')
    password1 = request.form.get('psw')
    password2 = request.form.get('psw-repeat')
    name = request.form.get('BN')
    CompanyID = request.form.get('bid')
    user = BusinessUser.query.filter_by(email=email).first()
    user1 = User.query.filter_by(email=email).first()
    user2 = BusinessUser.query.filter_by(email=email).first()
    user3 = AssociationUser.query.filter_by(email=email).first()
    if user1 or user2 or user3:
        # user exists
        return render_template("registerbussines.html", exists=True)
    if password1!=password2:
        flag=False
        return render_template("register.html")


    if request.method == 'POST' and email and password1:
        new_user = BusinessUser(email=email, password=password1, name=name, CompanyID=CompanyID)
        db.session.add(new_user)
        db.session.commit()

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