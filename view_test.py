from operator import index
from werkzeug.wrappers import response
from GetPet import create_app
from GetPet.models import User,BusinessUser,AssociationUser
from GetPet.auth import register
from GetPet.auth import login
import unittest
from flask import render_template,Flask
from urllib.parse import urlparse,ParseResult
import pytest,json
from GetPet import views as flask_app




@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200
  

""" app = Flask(__name__)

from GetPet.views import views

app.register_blueprint(views, url_prefix='')

class BluePrintTestCase(unittest.TestCase):

    def setUp(self):
        self.app = views.test_client()

    def test_health(self):
        rv = self.app.get('GetPet\views.py')
        print (rv.data)
 """








"""class TestMyApp(unittest.TestCase):
    def create_app(self):
        self.app = views.test_client()



    def test_main(self):
        tester = views.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')
    """





if __name__ == '__main__':
    unittest.main()