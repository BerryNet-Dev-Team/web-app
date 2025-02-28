import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from .database.dbConnection import db
from .database.serializers_utils import ma
from .security.bcrypt import bcrypt
from .routes.errorHandlers import errorHandlers

# load .env file to environment
load_dotenv()

# Import routers
from .routes.auth import auth
from .routes.scenes import scenes
from .routes.inferences import inferences

migrate = Migrate()  # Creates an instance of migrate without initialization

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

    # Close DB session after each request
    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.close()
        db.session.remove()

    #Setup serializer
    ma.init_app(app)

    # Configure migrations
    migrate.init_app(app, db)  # Associates Flask-Migrate to the app

    # Configure flask_bcrypt utility
    bcrypt.init_app(app)

    # Register http error handlers
    app.register_blueprint(errorHandlers)

    # Register routers blueprints
    app.register_blueprint(auth)
    app.register_blueprint(scenes)
    app.register_blueprint(inferences)

    # Setup cors policies
    app.config['CORS_EXPOSE_HEADERS'] = ['Authorization']
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    CORS(app, resources={r"/*": {"origins": "*"}}, expose_headers=['Authorization'])

    print('Runing apppp')
    return app
