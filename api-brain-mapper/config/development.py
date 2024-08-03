import os
from dotenv import load_dotenv

load_dotenv()    

class DevelopmentConfig(object):
    TESTING = False
    DEBUG = True
    SECRET_KEY=os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_URL')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACKS_MODIFICATIONS = False