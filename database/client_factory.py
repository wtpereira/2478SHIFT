from pymongo import MongoClient
from pymongo.server_api import ServerApi

from settings import (
    MONGODB_HOST,
    MONGODB_USERNAME,
    MONGODB_PASSWORD,
)


class ClientFactory:
    def get_client(self):
        return MongoClient(
            f'mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}/?retryWrites=true&w=majority&appName=Cluster0',
            server_api=ServerApi('1')
        )
