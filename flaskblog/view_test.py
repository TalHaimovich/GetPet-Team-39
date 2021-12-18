
from GetPet import create_app
import unittest
import pytest,json


#route testing using pytest, for actrivation enter the folowing line on terminal " python -m pytest"
#you need to have pytest installed by folowing line on terminal "python -m pip install pytest --verbose"
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200
  


if __name__ == '__main__':
    unittest.main()