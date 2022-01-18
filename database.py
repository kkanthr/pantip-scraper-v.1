from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class MongoDB(object):
    def __init__(self):
        self.host = os.getenv('MONGODB_HOST')
        self.port = int(os.getenv('MONGODB_PORT'))
        self.username = os.getenv('MONGODB_USERNAME')
        self.password = os.getenv('MONGODB_PASSWORD')
        self.db_name = os.getenv('MONGODB_DB_NAME')
        self.coll_name = os.getenv('MONGODB_COLL_NAME')
    
    def connect(self):
        client = MongoClient( host=self.host,
                              port=self.port,
                              username=self.username,
                              password=self.password)

        database = client[self.db_name]
        collection = database[self.coll_name]

        return collection