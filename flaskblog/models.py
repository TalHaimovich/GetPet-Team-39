from datetime import datetime
from flaskblog import db
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

class User(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)


    ### For easier access
    bus_user    = db.relationship('BusUser',  back_populates='user', uselist=False)
    asos_user   = db.relationship('AsosUser', back_populates='user', uselist=False)

    @hybrid_property
    def is_bus_user(self):
        return self.bus_user != None

    @hybrid_property
    def is_asos_user(self):
        return self.asos_user != None

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class BusUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', uselist=False)

    bus_name = db.Column(db.String(20),unique=True,nullable=False)
    bus_id = db.Column(db.String(20),unique=True,nullable=False)

    def __repr__(self):
        return f"BusUser('{self.bus_name}','{self.user}')"


class AsosUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', uselist=False)

    asos_name = db.Column(db.String(20),unique=True,nullable=False)
    asos_addres = db.Column(db.String(20),unique=True,nullable=False)
    

    def __repr__(self):
        return f"AsosUser('{self.asos_name}','{self.user}')"


class Post(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text , nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
     
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')" 

# class BusPost(db.Model):
#     id = db.Column(db.Integer ,primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text , nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('bus_user.id'),nullable=False)
     
#     def __repr__(self):
#         return f"BusPost('{self.title}','{self.date_posted}')" 

# class AsosPost(db.Model):
#     id = db.Column(db.Integer ,primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text , nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('asos_user.id'),nullable=False)
     
#     def __repr__(self):
#         return f"AsosPost('{self.title}','{self.date_posted}')" 
