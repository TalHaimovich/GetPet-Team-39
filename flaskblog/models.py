from datetime import datetime
from flaskblog import db

class User(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post', backref ='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class BusUser(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    bus_name = db.Column(db.String(20),unique=True,nullable=False)
    bus_id = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('BusPost', backref ='author', lazy=True, primaryjoin="User.id == Post.bususer_id")

    def __repr__(self):
        return f"BusUser('{self.bus_name}','{self.email}','{self.image_file}')"


class AsosUser(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    asos_name = db.Column(db.String(20),unique=True,nullable=False)
    asos_addres = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('AsosPost', backref ='author', lazy=True,primaryjoin="User.id == Post.asosuser_id")

    def __repr__(self):
        return f"AsosUser('{self.asos_name}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text , nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
     
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')" 

class BusPost(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text , nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
     
    def __repr__(self):
        return f"BusPost('{self.title}','{self.date_posted}')" 

class AsosPost(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text , nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
     
    def __repr__(self):
        return f"AsosPost('{self.title}','{self.date_posted}')" 
