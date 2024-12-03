import dotenv
import os

# import motor.motor_asyncio

# client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('MONGODB_URL'))

# print(client)


from pymongo import MongoClient
dotenv.load_dotenv()
MONGO_URL = os.getenv('MONGODB_URL')


def mongo_client(db_name,db_collection):
    client = MongoClient(MONGO_URL)
    db = client[db_name]
    collection = db[db_collection]
    return collection