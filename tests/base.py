from flask_testing import TestCase
from flaskblog import app, bcrypt
from flaskblog.models import *


class BaseTestCase(TestCase):
    render_templates = False

    def setUp(self) -> None:
        User.query.filter().delete()
        Post.query.filter().delete()
        db.session.commit()

    def create_app(self):
        app.config["TESTING"] = True
        app.testing = True

        # This creates an in-memory sqlite db
        # See https://martin-thoma.com/sql-connection-strings/
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()
        with app.app_context():
            db.create_all()
            db.session.commit()

        return app

    def create_test_user(self, name, email, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(password=hashed_password, email=email, name=name)
        db.session.add(user)
        db.session.commit()
        return user

    def login_test_user(self, email, password):
        response = self.client.post("/login", data={'email': email, 'password': password})
        self.assertRedirects(response, '/home_in')

    def creat_test_post(self,title,user_id,content):
        post = Post(title=title, user_id=user_id, content=content)
        db.session.add(post)
        db.session.commit()
        return post

# def test_assert_mytemplate_used(self):
#     response = self.client.get("/registeruser")
#     assert response.status_code == 200
#     self.assert_template_used('registeruser.html')
#     self.assert_context('test', User.query.all())
