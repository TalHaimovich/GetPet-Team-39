from flaskblog.models import *
from .base import BaseTestCase


class UserTests(BaseTestCase):
    #test creation of a new user (test User "Ctor")
    def test_User(self):
        new_user=User(name="yosi",id=123,email="aaa@gmail.com", password="12345")
        assert new_user.password=="12345","should be equal"
        assert new_user.email=="aaa@gmail.com", "should be equal"
        assert new_user.id==123, "should be equal"
        assert new_user.name=="yosi", "should be equal"
        assert new_user.id!=1345, "should not be equal"
        assert new_user.is_asos != True ,"should not be equal"
        assert new_user.is_bus != True , "should not be equal"
        assert new_user.is_admin != True,"should not be equal" 

     #test creation of a new bussines user (test User "Ctor"+ bus_id + is_bus flag)
    def test_bussines_User(self):
        new_user = User(name="Jhon", email="asd@walla.com", password="234", bus_id=4567, is_bus=True)
        assert new_user.password=="234","should be equal"
        assert new_user.email=="asd@walla.com", "should be equal"
        assert new_user.bus_id==4567, "should be equal"
        assert new_user.bus_id!=1345, "should not be equal"
        assert new_user.is_bus==True, "should be equal"     #check the flag that indicate of bussines user
        assert new_user.is_asos != True,"should not be equal"
        assert new_user.is_admin != True,"should not be equal"
        assert new_user.name=="Jhon", "should be equal"

    #test creation of a new assosiationuser user (test User "Ctor"+ address + is_asos flag)
    def test_assosiation_User(self):
        new_user = User(name="Jim", email="avvv@yahooo.com", password="xzy456", address="Beer-Sheva", is_asos=True)
        assert new_user.password=="xzy456","should be equal"
        assert new_user.email=="avvv@yahooo.com", "should be equal"
        assert new_user.address=="Beer-Sheva", "should be equal"
        assert new_user.name=="Jim", "should be equal"
        assert new_user.address!="Dimona", "should not be equal"
        assert new_user.is_asos==True, "should be equal"     #check the flag that indicate of assosiationuser user

    def test_register_user(self):
        response = self.client.post(
            "/registeruser",
            data={'name': 'test',
                  'email': 'asd@asd.com',
                  'password': 'pass1234',
                  'confirm_password': 'pass1234'},
        )
        self.assertRedirects(response, '/login')
        self.assertEqual(User.query.count(), 1)
        user = User.query.first()
        self.assertEqual(user.name, 'test')
        self.assertEqual(user.email, 'asd@asd.com')
        self.assertIsNotNone(user.password)
        self.assertEqual(user.image, 'default.jpg')


    def test_register_business_user(self):
        response = self.client.post(
            "/registerbusiness",
            data={'name': 'test','bus_id':'1234',
                  'email': 'asd@asd.com',
                  'password': 'pass1234',
                  'confirm_password': 'pass1234'},
        )
        self.assertRedirects(response, '/login')
        self.assertEqual(User.query.count(), 1)
        user = User.query.first()
        self.assertEqual(user.name, 'test')
        self.assertEqual(user.bus_id, 1234)
        self.assertEqual(user.email, 'asd@asd.com')
        self.assertIsNotNone(user.password)
        self.assertEqual(user.image, 'default.jpg')


    def test_register_asos_user(self):
        response = self.client.post(
            "/registerassociation",
            data={'name': 'test','address':'test adress',
                  'email': 'asd@asd.com',
                  'password': 'pass1234',
                  'confirm_password': 'pass1234'},
        )
        self.assertRedirects(response, '/login')
        self.assertEqual(User.query.count(), 1)
        user = User.query.first()
        self.assertEqual(user.name, 'test')
        self.assertEqual(user.address, 'test adress')
        self.assertEqual(user.email, 'asd@asd.com')
        self.assertIsNotNone(user.password)
        self.assertEqual(user.image, 'default.jpg')    

    def test_login(self):
        self.create_test_user('test', 'asd@asd.com', 'pass')
        response = self.client.post("/login", data={'email': 'asd@asd.com', 'password': 'pass'})
        self.assertRedirects(response, '/home_in')

    def test_send_pet_coin(self):
        send_user = self.create_test_user('send', 'send@asd.com', 'pass')
        recv_user = self.create_test_user('recv', 'recv@asd.com', 'pass')
        self.login_test_user('send@asd.com', 'pass')
        response = self.client.post("/send_pet_coin", data={'email': 'recv@asd.com', 'amount': 50},
                                    headers={"Referer": '/home_in'})
        self.assertRedirects(response, '/home_in')
        self.assertEqual(recv_user.pet_coin, 100)
        self.assertEqual(send_user.pet_coin, 0)
