from flaskblog.models import *
from .base import BaseTestCase



class RoutsTests(BaseTestCase):

    def test_home(self):
        rv = self.client.get("/home")
        self.assertNotEqual(rv.status_code, 401)
        self.assertNotEqual(rv.status_code, 305)   
        self.assertNotEqual(rv.status_code, 401)
        self.assert200(rv) 
        self.assertEqual(rv.status_code,200)

               

    def test_about(self):
        rv = self.client.get("/about")
        self.assertNotEqual(rv.status_code, 401)
        self.assert200(rv) 
        self.assertEqual(rv.status_code,200)

    def test_register(self):
        rv = self.client.get("/register")
        self.assertNotEqual(rv.status_code, 401)
        self.assertNotEqual(rv.status_code, 305)      
        self.assert200(rv) 
        self.assertEqual(rv.status_code,200)

    def test_registeruser(self):
        rv = self.client.get("/registeruser")
        self.assertNotEqual(rv.status_code, 401)
        self.assertNotEqual(rv.status_code, 301)      
        self.assert200(rv) 
        self.assertEqual(rv.status_code,200)           

    def test_registerbusiness(self):
        rv = self.client.get("/registerbusiness")
        self.assertNotEqual(rv.status_code, 401)
        self.assert200(rv) 
        self.assertNotEqual(rv.status_code, 303)      
        self.assertEqual(rv.status_code,200)  


    def test_registerassociation(self):
        rv = self.client.get("/registerassociation")
        self.assertNotEqual(rv.status_code, 401)
        self.assertNotEqual(rv.status_code, 303)      
        self.assert200(rv) 
        self.assertEqual(rv.status_code,200)

    def test_login(self):
        rv = self.client.get("/login")
        self.assertNotEqual(rv.status_code, 401)      
        self.assert200(rv) 
        self.assertEqual(rv.status_code,200)

    def test_logout(self):
        rv = self.client.get("/logout")
        self.assertNotEqual(rv.status_code, 401)
        self.assertNotEqual(rv.status_code, 303)      
        self.assertEqual(rv.status_code,302) 
        self.assertNotEqual(rv.status_code,200)            
 

    def test_send_pet_coin(self):
        test_user = self.create_test_user('test', 'test@asd.com', 'pass')
        self.login_test_user('test@asd.com', 'pass')
        rv = self.client.get('/send_pet_coin')
        self.assertNotEqual(rv.status_code, 401)
        self.assertNotEqual(rv.status_code, 303)     
        self.assert405(rv) 
        self.assertEqual(rv.status_code,405)   #should get 405 because the route have "POST" method only
        self.assertNotEqual(rv.status_code,305)   

    def test_home_in(self):
        test_user = self.create_test_user('test', 'test@asd.com', 'pass')
        self.login_test_user('test@asd.com', 'pass')
        rv = self.client.get("/home_in")
        self.assertNotEqual(rv.status_code, 401)
        self.assert200(rv) 
        self.assertNotEqual(rv.status_code, 303)      
        self.assertEqual(rv.status_code,200) 
        self.assertNotEqual(rv.status_code,305)    


    def test_reports(self):
        test_user = self.create_test_user('test', 'test@asd.com', 'pass')
        self.login_test_user('test@asd.com', 'pass')
        rv = self.client.get("/reports")
        self.assertNotEqual(rv.status_code, 401)
        self.assert200(rv) 
        self.assertNotEqual(rv.status_code, 303)      
        self.assertEqual(rv.status_code,200) 
        self.assertNotEqual(rv.status_code,401)   


    def test_delete_post(self):
        test_user = self.create_test_user('test', 'test@asd.com', 'pass')
        self.login_test_user('test@asd.com', 'pass')
        post = self.creat_test_post('test',test_user.id,'content')  #creat post for later commit to db
        str_id=str(post.id)
        rv = self.client.get('/delete_post/'+str_id)
        self.assertNotEqual(rv.status_code, 401)
        self.assertNotEqual(rv.status_code, 303)     
        self.assert405(rv) 
        self.assertEqual(rv.status_code,405)   #should get 405 because the route have "POST" method only
        self.assertNotEqual(rv.status_code,200)   

    def test_create_post(self):
        test_user = self.create_test_user('test', 'test@asd.com', 'pass')
        self.login_test_user('test@asd.com', 'pass')
        rv = self.client.get('/create_post')
        self.assertNotEqual(rv.status_code, 200)
        self.assertNotEqual(rv.status_code, 305)     
        self.assert405(rv) 
        self.assertEqual(rv.status_code,405)   #should get 405 because the route have "POST" method only
        self.assertNotEqual(rv.status_code,305)   


    def test_update_post(self):
        test_user = self.create_test_user('test', 'test@asd.com', 'pass')
        self.login_test_user('test@asd.com', 'pass')
        post = self.creat_test_post('test',test_user.id,'content')  #creat post for later commit to db
        str_id=str(post.id)
        rv = self.client.get('/update_post/'+str_id)
        self.assertNotEqual(rv.status_code, 305)
        self.assertNotEqual(rv.status_code, 200)     
        self.assert405(rv) 
        self.assertEqual(rv.status_code,405)   #should get 405 because the route have "POST" method only
        self.assertNotEqual(rv.status_code,305)   

    def test_report_post(self):
        test_user = self.create_test_user('test', 'test@asd.com', 'pass')
        test_user2 = self.create_test_user('test', 'send@asd.com', 'pass')
        self.login_test_user('send@asd.com', 'pass')
        post = self.creat_test_post('test',test_user2.id,'content')  #creat post for later commit to db
        str_id=str(post.id)
        rv = self.client.get('/report_post/'+str_id)
        self.assertNotEqual(rv.status_code, 305)
        self.assertNotEqual(rv.status_code, 200)     
        self.assert405(rv) 
        self.assertEqual(rv.status_code,405)   #should get 405 because the route have "POST" method only
        self.assertNotEqual(rv.status_code,22)   


    def test_account(self):
        test_user = self.create_test_user('test', 'test@asd.com', 'pass')
        self.login_test_user('test@asd.com', 'pass')
        rv = self.client.get("/account")
        self.assertNotEqual(rv.status_code, 401)
        self.assert200(rv) 
        self.assertNotEqual(rv.status_code, 303)      
        self.assertEqual(rv.status_code,200) 
        self.assertNotEqual(rv.status_code,305)    


    def test_asosnews(self):
        test_user = self.create_test_user('test', 'test@asd.com', 'pass')
        self.login_test_user('test@asd.com', 'pass')
        rv = self.client.get("/association_news")
        self.assertNotEqual(rv.status_code, 401)
        self.assert200(rv) 
        self.assertNotEqual(rv.status_code, 303)      
        self.assertEqual(rv.status_code,200) 
        self.assertNotEqual(rv.status_code,305)   


    def test_busupdate(self):
        test_user = self.create_test_user('test', 'test@asd.com', 'pass')
        self.login_test_user('test@asd.com', 'pass')
        rv = self.client.get("/business_news")
        self.assertNotEqual(rv.status_code, 401)
        self.assert200(rv) 
        self.assertNotEqual(rv.status_code, 303)      
        self.assertEqual(rv.status_code,200) 
        self.assertNotEqual(rv.status_code,305)   



