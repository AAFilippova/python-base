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

    def test_index(self, client):
        response = client.get('/')
        assert response.status_code == 200
    def test_information(self, client):
        response = client.get('/information')
        assert response.status_code == 200
        assert b'<h1>' in response.data
        assert b'<table' in response.data


    def test_add_user_to_information(self, client):
        username = f"user-{uuid.uuid4()}"
        email = f"{uuid.uuid4()}@ya.ru"
        response = client.post('/add_users', data={
            'name': 'fedor',
             'username': username,
             'email': email
         }, follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/information'