from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    
    # Create tables if they do not exist
    with app.app_context():
        db.create_all()
    
    # Register blueprints
    from app.views import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
