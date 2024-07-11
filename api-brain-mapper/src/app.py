import os
from dotenv import load_dotenv
from flask import Flask
from .database.dbConnection import db
from .routes.errorHandlers import errorHandlers

# load .env file to environment
load_dotenv()

# Import routers
from .routes.auth import auth

def create_app():
    # Create Flask app
    app = Flask(__name__)

    # Configure app depending on environment mode
    if(os.getenv('ENV_MODE') == 'production'):
        from config.production import ProductionConfig
        app.config.from_object(ProductionConfig)
    else:
        from config.development import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)

    # Starts db connection
    db.init_app(app)

    # Register http error handlers
    app.register_blueprint(errorHandlers)

    # Register routers blueprints
    app.register_blueprint(auth)

    # Give context to SQLAlchemy
    with app.app_context():
        db.create_all()

    return app
