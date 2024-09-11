import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


connection_string = os.getenv("MONGO_CONNECTION_STRING")

def get_titles_for_email(email: str) -> list[str]:
    client = MongoClient(connection_string, server_api=ServerApi('1'))
    try:        
        db = client['email-assistant']
        lecturers = db['lecturers']
        user = lecturers.find_one({ "email" : email })
        
        return [] if user is None else user['titles']
    except Exception as e:
        print(e)
        
    return []