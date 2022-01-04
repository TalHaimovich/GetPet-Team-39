from flaskblog.models import *
from .base import BaseTestCase


class PostTests(BaseTestCase):
    def setUp(self) -> None:
        super(PostTests, self).setUp()
        self.user = self.create_test_user('test', 'asd@asd.com', 'pass')
        self.login_test_user('asd@asd.com', 'pass')
        db.session.commit()

    #test creation of new postf by the model via post ctor
    def test_new_post(self):
        new_post=Post(id=112233,user_id=56789,title="Testing-Post",content="Post-Content",date_posted='April 21, 2018')
        assert new_post.id==112233,"should be equal"
        assert new_post.user_id==56789,"should be equal"
        assert new_post.title=="Testing-Post","should be equal"
        assert new_post.content=="Post-Content","should be equal"
        assert new_post.date_posted=='April 21, 2018'
        assert new_post.id != 1234, "should not be equal"
        assert new_post.user_id!=12212,"should not be equal"
        assert new_post.is_foster!=True, "should not be equal"
        assert new_post.is_discount!=True, "should not be equal"
        assert new_post.is_adopt!=True , "should not be equal"
        assert new_post.is_product!=True, "should not be equal"
        assert new_post.is_events!=True, "should not be equal"    

    #  #test for making another type of post in the db
    def test_new_adopt_post(self):
        new_post=Post(id=435,user_id=69089,title="Testing-test",content="Post-post",date_posted='April 21, 2018',is_adopt=True)
        assert new_post.id==435,"should be equal"
        assert new_post.user_id==69089,"should be equal"
        assert new_post.title=="Testing-test","should be equal"
        assert new_post.content=="Post-post", "should be equal"
        assert new_post.date_posted=='April 21, 2018'
        assert new_post.id != 1234, "should not be equal"
        assert new_post.user_id!=12212, "should not be equal"
        assert new_post.is_foster!=True, "should not be equal"
        assert new_post.is_events!=True ,"should not be equal"
        assert new_post.is_adopt==True, "should be equal"  #check the flag that indicate of adopt post   

    def test_create_post(self):
        post = Post(title='test', user_id=self.user.id, content='content')
        db.session.add(post)
        db.session.commit()
        response = self.client.get('/home_in')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('homelogged.html')
        self.assertEqual(self.get_context_variable('all_posts').count(), 1)

    def test_delete_post(self):
        post = Post(title='test', user_id=self.user.id, content='content')
        db.session.add(post)
        db.session.commit()
        self.assertEqual(Post.query.count(), 1)
        response = self.client.post('/delete_post/'+str(post.id), headers={"Referer": '/home_in'})
        self.assertRedirects(response, '/home_in')
        self.assertEqual(Post.query.count(), 0)


    def test_new_event_post(self):
        new_events=Post(id=480,user_id=66089,title="Testing-test",content="Post-post",date_posted='April 21, 2018',is_events=True)
        assert new_events.id==480,"should be equal"
        assert new_events.user_id==66089,"should be equal"
        assert new_events.title=="Testing-test","should be equal"
        assert new_events.content=="Post-post", "should be equal"
        assert new_events.date_posted=='April 21, 2018'
        assert new_events.id != 1234, "should not be equal"
        assert new_events.user_id!=12212, "should not be equal"
        assert new_events.is_foster!=True, "should not be equal"
        assert new_events.is_events==True ,"should  be equal"
        assert new_events.is_adopt!=True, "should not be equal"  #check the flag that indicate of events post 
