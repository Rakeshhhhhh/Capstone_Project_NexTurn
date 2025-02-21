from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()  # Declare db here first

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # Import routes here after initializing db
    with app.app_context():
        db.create_all()
        
    return app
