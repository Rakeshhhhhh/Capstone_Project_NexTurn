import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def app():
    # Create a test Flask app
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    # Set up the database
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()

def test_user_creation(app):
    # Test creating a new user
    with app.app_context():
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()

        # Retrieve the user from the database
        retrieved_user = User.query.filter_by(username='testuser').first()
        assert retrieved_user is not None
        assert retrieved_user.email == 'test@example.com'

def test_user_update(app):
    # Test updating a user
    with app.app_context():
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()

        # Update the user
        user.username = 'updateduser'
        user.email = 'updated@example.com'
        db.session.commit()

        # Retrieve the updated user
        updated_user = User.query.filter_by(username='updateduser').first()
        assert updated_user is not None
        assert updated_user.email == 'updated@example.com'

def test_user_deletion(app):
    # Test deleting a user
    with app.app_context():
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()

        # Delete the user
        db.session.delete(user)
        db.session.commit()

        # Verify the user is deleted
        deleted_user = User.query.filter_by(username='testuser').first()
        assert deleted_user is None