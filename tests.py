from unittest.case import _AssertRaisesContext
from flaskblog.models import User,Post
from flaskblog.forms import RegistrationForm,BusRegistrationForm,AsosRegistrationForm
import unittest
from flask import Flask



#users testing-using unittest,for activation run that file
class test_models(unittest.TestCase):



    def test_new_post(self):
        new_post=Post(id=112233,user_id=56789,title="Testing-Post",content="Post-Content",date_posted='April 21, 2018')
        assert new_post.id==112233
        assert new_post.user_id==56789
        assert new_post.title=="Testing-Post"
        assert new_post.content=="Post-Content"
        assert new_post.date_posted=='April 21, 2018'
        assert new_post.id != 1234
        assert new_post.user_id!=12212

    #test creation of a new user (test User "Ctor")
    def test_User(self):
        new_user=User(name="yosi",id=123,email="aaa@gmail.com", password="12345")
        assert new_user.password=="12345","should be equal"
        assert new_user.email=="aaa@gmail.com", "should be equal"
        assert new_user.id==123, "should be equal"
        assert new_user.name=="yosi", "should be equal"
        assert new_user.id!=1345, "should not be equal"



        #test creation of a new bussines user (test User "Ctor"+ bus_id + is_bus flag)
    def test_bussines_User(self):
        new_user = User(name="Jhon", email="asd@walla.com", password="234", bus_id=4567, is_bus=True)
        assert new_user.password=="234","should be equal"
        assert new_user.email=="asd@walla.com", "should be equal"
        assert new_user.bus_id==4567, "should be equal"
        assert new_user.bus_id!=1345, "should not be equal"
        assert new_user.is_bus==True, "should be equal"     #check the flag that indicate of bussines user
        assert new_user.name=="Jhon", "should be equal"    
    

if __name__ == '__main__':
    unittest.main()