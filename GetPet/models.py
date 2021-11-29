
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

"""data base calss for regular users,including a primary id.
every user will have only one specific id number"""
class User(db.Model,UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(100), unique=True)
    password=db.Column(db.String(150))

"""data base class for business users,including a "unique" company id.
every business user will have only one specific company id.
bussines user will have the regular user fileds as well"""
class BusinessUser(db.Model,UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    CompanyID=db.Column(db.Integer)
    email=db.Column(db.String(100), unique=True)
    name=db.Column(db.String(150))
    password=db.Column(db.String(150))



"""data base class for business users,including a "unique" adress.
every Association user will have only one specific adress.
bussines user will have the regular user fileds as well"""
class AssociationUser(db.Model,UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(100), unique=True)
    name=db.Column(db.String(150))
    password=db.Column(db.String(150))
    adress=db.Column(db.String(150), unique=True)


