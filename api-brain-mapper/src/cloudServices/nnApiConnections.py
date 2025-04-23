import os
from dotenv import load_dotenv
import requests
import jwt
import uuid
from datetime import datetime, timedelta, timezone
load_dotenv()

class NnAPIClient:
    def __init__(self, base_url, secret_key):
        """
        Initialize the client that will communicate with NN API
        :param base_url: Base URL of API (eg: 'https://api.neuralnetwork.com/v1')
        :param secret_key: Secret key for NN API
        """
        self.base_url = base_url
        self.secret_key = secret_key


    def _generateToken(self):
        jti = str(uuid.uuid4())
        now = datetime.now(timezone.utc)

        payload = {
            'jti': jti,
            'iat': now,
            'exp': now + timedelta(seconds=30)
        }

        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token
    
    def generateInference(self, data=None):
        token = self._generateToken()
        url = f"{self.base_url}/inferencia"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()