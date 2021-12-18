from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

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

    


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
