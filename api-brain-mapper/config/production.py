import os
from dotenv import load_dotenv

load_dotenv()    

class ProductionConfig(object):
    TESTING = False
    DEBUG = False
    SECRET_KEY=os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_URL')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACKS_MODIFICATIONS = False

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 2000,      # MAX 2000 pool size
        "pool_recycle": 1800,   # Close connections after 30 mins
        "pool_timeout": 15,     # Wait 15 seconds before failing to get connected 
        "max_overflow": 5       # Permits 5 extra connections
    }