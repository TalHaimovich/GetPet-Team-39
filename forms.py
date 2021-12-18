from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User,BusUser,AsosUser

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user= User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That username is taken. please choose another')
    def validate_email(self, email):
            user= User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('That email is taken. please choose another')



class RegistrationFormBUS(FlaskForm):
    bus_name = StringField('שם עסק',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    bus_id=StringField('bus_id',
                        validators=[DataRequired(), Length(min=1,max=20)])
    submit = SubmitField('Sign Up')

    
    def validate_bus_name(self, bus_name):
        user= BusUser.query.filter_by(bus_name = bus_name.data).first()
        if user:
            raise ValidationError('That username is taken. please choose another')
    def validate_email(self, email):
            user= User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('That email is taken. please choose another')


class RegistrationFormAsso(FlaskForm):
    asos_name = StringField('שם אגודה',
                           validators=[DataRequired(), Length(min=2, max=20)])
    asos_addres = StringField('כתובת',
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('אימייל',
                        validators=[DataRequired(), Email()])
    password = PasswordField('סיסמא', validators=[DataRequired()])
    confirm_password = PasswordField('חזור על הסיסמא',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('הירשם')############

    def validate_asos_name(self, asos_name):
        user= AsosUser.query.filter_by(asos_name = asos_name.data).first()
        if user:
            raise ValidationError('That username is taken. please choose another')
    def validate_email(self, email):
            user= User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('That email is taken. please choose another')



class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
