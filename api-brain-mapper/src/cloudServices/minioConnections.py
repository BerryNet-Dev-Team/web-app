import os
from dotenv import load_dotenv
from minio import Minio
load_dotenv()

def getMinioClient():
    return Minio(
        endpoint=os.getenv('S3_HOST'),
        secure=(os.getenv('ENV_MODE') == "production"),
        access_key=os.getenv('S3_ACCESS_KEY'),
        secret_key=os.getenv('S3_SECRET_KEY'),
    )