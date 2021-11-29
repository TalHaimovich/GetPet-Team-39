
from GetPet import create_app
import unittest
import pytest,json





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