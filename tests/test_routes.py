import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    # Create a test Flask app
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    # Set up the database
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_user(client):
    # Test creating a new user
    response = client.post('/users/create', data={
        'username': 'testuser',
        'email': 'test@example.com'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'testuser' in response.data

def test_get_user(client):
    # Create a user first
    client.post('/users/create', data={
        'username': 'testuser',
        'email': 'test@example.com'
    }, follow_redirects=True)

    # Test retrieving the user
    response = client.get('/users/1')
    assert response.status_code == 200
    assert b'testuser' in response.data

def test_update_user(client):
    # Create a user first
    client.post('/users/create', data={
        'username': 'testuser',
        'email': 'test@example.com'
    }, follow_redirects=True)

    # Test updating the user
    response = client.post('/users/1/edit', data={
        'username': 'updateduser',
        'email': 'updated@example.com'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'updateduser' in response.data

def test_delete_user(client):
    # Create a user first
    client.post('/users/create', data={
        'username': 'testuser',
        'email': 'test@example.com'
    }, follow_redirects=True)

    # Test deleting the user
    response = client.delete('/users/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'testuser' not in response.data

