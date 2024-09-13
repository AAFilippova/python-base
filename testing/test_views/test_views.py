import uuid
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

class TestViews:
    def test_index(self, client):
        response = client.get('/')
        assert response.status_code == 200


    def test_information(self, client):
        response = client.get('/information')
        assert response.status_code == 200

