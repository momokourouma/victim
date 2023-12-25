from pydantic import EmailStr
from pymongo import MongoClient

from ModelVictime import VictimeModel

# client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mohamed:Jackmah1998@ac-mcvyv4w-shard-00-00.juoab6m.mongodb.net:27017,ac-mcvyv4w-shard-00-01.juoab6m.mongodb.net:27017,ac-mcvyv4w-shard-00-02.juoab6m.mongodb.net:27017/?ssl=true&replicaSet=atlas-5evec0-shard-0&authSource=admin&retryWrites=true&w=majority")
client = MongoClient("mongodb://mohamed:Jackmah1998@ac-mcvyv4w-shard-00-00.juoab6m.mongodb.net:27017,ac-mcvyv4w-shard-00-01.juoab6m.mongodb.net:27017,ac-mcvyv4w-shard-00-02.juoab6m.mongodb.net:27017/?ssl=true&replicaSet=atlas-5evec0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["Victime"]
collection = db["VictimeCollection"]


# Authentification

def CreateAuth(Username: EmailStr, Password: str):
    return {"message": "User created"}




# Adding users to the database

def AddUser(user: VictimeModel):
    new_user = collection.insert_one(user.dict())
    return {"message": new_user.inserted_id}


# Updating user
def UpdateUser(id: str):
    return {"message": "updated"}


# delete User

def DeleteUser(id: str):
    return {"message": "updated"}
