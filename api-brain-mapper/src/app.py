import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from .database.dbConnection import db
from .database.serializers_utils import ma
from .routes.errorHandlers import errorHandlers

# load .env file to environment
load_dotenv()

# Import routers
from .routes.auth import auth
from .routes.scenes import scenes

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

    #Setup serializer
    ma.init_app(app)

    # Configure migrations
    migrate = Migrate(app, db)

    # Register http error handlers
    app.register_blueprint(errorHandlers)

    # Register routers blueprints
    app.register_blueprint(auth)
    app.register_blueprint(scenes)

    # Setup cors policies
    app.config['CORS_EXPOSE_HEADERS'] = ['Authorization']
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    CORS(app, resources={r"/*": {"origins": "*"}}, expose_headers=['Authorization'])

    # Give context to SQLAlchemy
    with app.app_context():
        db.create_all()

    return app
