import os
from dotenv import load_dotenv

load_dotenv()    

class ProductionConfig(object):
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_URL')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACKS_MODIFICATIONS = False