import os
from dotenv import load_dotenv

load_dotenv()    

class DevelopmentConfig(object):
    TESTING = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlclientconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_URL')}/{os.getenv('DB_NAME')}"

    SQLALCHEMY_TRACKS_MODIFICATIONS = False