<<<<<<< HEAD
from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image = db.Column(db.String(100), nullable=False, default='default.jpg')
    address = db.Column(db.String(100), nullable=True)
    bus_id = db.Column(db.Integer, nullable=True)
    is_bus = db.Column(db.Boolean, default=False, nullable=False)  # true if user is business user
    is_asos = db.Column(db.Boolean, default=False, nullable=False)  # true if user is asos user
    is_admin = db.Column(db.Boolean, default=False, nullable=False)  # true if user is admin user

    posts = db.relationship('Post', backref='user')

    def __repr__(self):
        return f"User('{self.name}','{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image = db.Column(db.String(100), nullable=False, default='default.jpg')
    price = db.Column(db.Integer, nullable=False, default=0)

    is_adopt = db.Column(db.Boolean, default=False, nullable=False)
    is_foster = db.Column(db.Boolean, default=False, nullable=False)
    is_product = db.Column(db.Boolean, default=False, nullable=False)
    is_discount = db.Column(db.Boolean, default=False, nullable=False)
        
    is_events = db.Column(db.Boolean, default=False, nullable=False)
    is_tips = db.Column(db.Boolean, default=False, nullable=False)


    def __repr__(self):
        return f"Post('{self.title}')"
=======
from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image = db.Column(db.String(100), nullable=False, default='default.jpg')
    address = db.Column(db.String(100), nullable=True)
    bus_id = db.Column(db.Integer, nullable=True)
    is_bus = db.Column(db.Boolean, default=False, nullable=False)  # true if user is business user
    is_asos = db.Column(db.Boolean, default=False, nullable=False)  # true if user is asos user
    is_admin = db.Column(db.Boolean, default=False, nullable=False)  # true if user is admin user

    posts = db.relationship('Post', backref='user')

    def __repr__(self):
        return f"User('{self.name}','{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image = db.Column(db.String(100), nullable=False, default='default.jpg')
    price = db.Column(db.Integer, nullable=False, default=0)

    is_adopt = db.Column(db.Boolean, default=False, nullable=False)
    is_foster = db.Column(db.Boolean, default=False, nullable=False)
    is_product = db.Column(db.Boolean, default=False, nullable=False)
    is_discount = db.Column(db.Boolean, default=False, nullable=False)
        
    is_events = db.Column(db.Boolean, default=False, nullable=False)
    is_tips = db.Column(db.Boolean, default=False, nullable=False)


    def __repr__(self):
        return f"Post('{self.title}')"
>>>>>>> 77f86eb11e8656f6315d2badc88d4195adba89aa
