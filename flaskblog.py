from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect,send_from_directory
from forms import RegistrationForm, LoginForm,RegistrationFormBUS,RegistrationFormAsso
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post', backref ='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Bus_User(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    bus_name = db.Column(db.String(20),unique=True,nullable=False)
    bus_id = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Bus_Post', backref ='author', lazy=True)

    def __repr__(self):
        return f"Bus_User('{self.bus_name}','{self.email}','{self.image_file}')"


class Asos_User(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    asos_name = db.Column(db.String(20),unique=True,nullable=False)
    asos_addres = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Asos_Post', backref ='author', lazy=True)


    def __repr__(self):
        return f"Asos_User('{self.asos_name}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text , nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
     
    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')" 

class Bus_Post(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text , nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
     
    def __repr__(self):
        return f"Bus_User('{self.title}','{self.date_posted}')" 

class Asos_Post(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text , nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
     
    def __repr__(self):
        return f"Asos_User('{self.title}','{self.date_posted}')" 

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

if __name__ == '__main__':
    app.run(debug=True)
