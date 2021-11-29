from werkzeug.wrappers import response
from GetPet import create_app
from GetPet.models import User,BusinessUser,AssociationUser
from GetPet.auth import register
from GetPet.auth import login
import unittest, pytest
from flask import render_template,Flask
from urllib.parse import urlparse,ParseResult


#route testing usin pytest
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_login(client):
    rv = client.get("/login")
    assert rv.status_code == 200        

def test_registeruser(client):
    rv = client.get("/registeruser")
    assert rv.status_code == 200        

def test_reg_asos(client):
    rv = client.get("/reg_asos")
    assert rv.status_code == 200     

def test_registerbussines(client):
    rv = client.get("/registerbussines")
    assert rv.status_code == 200     

def test_register(client):
    rv = client.get("/register")
    assert rv.status_code == 200    

def test_logout(client):
    rv = client.get("/logout")
    assert rv.status_code == 200        

      
#users testing-using unittest
class test_auth(unittest.TestCase):
    app=create_app()
    def create_app(self):
        app=Flask(__name__)
        app.config['TESTING']=True
        return app

  
    
    #test creation of a new user
    def test_new_user(self):
        new_user=User(id=123,email="aaa@gmail.com", password="12345")
        assert new_user.password=="12345","should be equal"
        assert new_user.email=="aaa@gmail.com", "should be equal"
        assert new_user.id==123, "should be equal"
        assert new_user.id!=1345, "should not be equal"

    #test creation of a new buasines user
    def test_new_bussinesuser(self):
        new_user=BusinessUser(CompanyID=6789, name="yosi",id=123,email="aaa@gmail.com", password="12345")
        assert new_user.password=="12345","should be equal"
        assert new_user.email=="aaa@gmail.com", "should be equal"
        assert new_user.id==123, "should be equal"
        assert new_user.id!=1345, "should not be equal"
        assert new_user.CompanyID==6789, "should be equal"
        assert new_user.name=="yosi", "should be equal"


    #test creation of a new AssociationUser user
    def test_new_assosiationuser(self):
        new_user=AssociationUser(adress="beer sheva", name="yosi",id=123,email="aaa@gmail.com", password="12345")
        assert new_user.password=="12345","should be equal"
        assert new_user.email=="aaa@gmail.com", "should be equal"
        assert new_user.id==123, "should be equal"
        assert new_user.id!=1345, "should not be equal"
        assert new_user.adress=="beer sheva", "should be equal"
        assert new_user.name=="yosi", "should be equal"

   
    

if __name__ == '__main__':
    unittest.main()