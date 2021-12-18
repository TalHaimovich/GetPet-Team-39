from flask import render_template, url_for, flash, redirect,send_from_directory
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm,RegistrationFormBUS,RegistrationFormAsso
from flaskblog.models import User, BusUser , AsosUser, Post, BusPost,AsosPost


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/images/<path:path>')
def serve_images(path):
    return send_from_directory('images', path)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    return render_template('register.html', title='Register')

@app.route("/registeruser", methods=['GET', 'POST'])
def registeruser():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registeruser.html', title='RegisterUser', form=form)


@app.route("/registerbus", methods=['GET', 'POST'])
def registerbus():
    form = RegistrationFormBUS()
    if form.validate_on_submit():
        flash(f'Account created for {form.bus_name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registerbus.html', title='RegisterBussines', form=form)

@app.route("/registerasos", methods=['GET', 'POST'])
def registerasos():
    form = RegistrationFormAsso()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registerasos.html', title='RegisterAssosition', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'a@a.com' and form.password.data == '1':
            flash('You have been logged in!', 'success')
            return redirect(url_for('homelogged'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/homelogged",methods=['GET','POST'])
def homelogged():
    return render_template('homelogged.html',title='homelogged',posts=posts)
