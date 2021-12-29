import os
import tempfile
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import pytest




from flaskblog.models import User,Post
import unittest, pytest
from flask import Flask
app = Flask(__name__)


from flaskblog import routes
#route testing using pytest, for actrivation enter the folowing line on terminal " python -m pytest"
#you need to have pytest installed by folowing line on terminal "python -m pip install pytest --verbose"

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    with app.test_client() as client:
        app.app_context()   
        yield client

    os.close(db_fd)
    os.unlink(db_path)


def test_home(client):
    rv = client.get("/home")
    assert rv.status_code == 200  

def test_login(client):
    rv = client.get("/login")
    assert rv.status_code == 200        

def test_registeruser(client):
    rv = client.get("/registeruser")
    assert rv.status_code == 404        

def test_reg_asos(client):
    rv = client.get("/reg_asos")
    assert rv.status_code == 404    

def test_registerbussines(client):
    rv = client.get("/registerbussines")
    assert rv.status_code == 404    

def test_register(client):
    rv = client.get("/register")
    assert rv.status_code == 404    

def test_logout(client):
    rv = client.get("/logout")
    assert rv.status_code == 404        

