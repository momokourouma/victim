from pymongo import MongoClient
import motor.motor_asyncio
#client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mohamed:Jackmah1998@ac-mcvyv4w-shard-00-00.juoab6m.mongodb.net:27017,ac-mcvyv4w-shard-00-01.juoab6m.mongodb.net:27017,ac-mcvyv4w-shard-00-02.juoab6m.mongodb.net:27017/?ssl=true&replicaSet=atlas-5evec0-shard-0&authSource=admin&retryWrites=true&w=majority")
#client = MongoClient("mongodb://mohamed:Jackmah1998@ac-mcvyv4w-shard-00-00.juoab6m.mongodb.net:27017,ac-mcvyv4w-shard-00-01.juoab6m.mongodb.net:27017,ac-mcvyv4w-shard-00-02.juoab6m.mongodb.net:27017/?ssl=true&replicaSet=atlas-5evec0-shard-0&authSource=admin&retryWrites=true&w=majority")
#db = client["Victime"]
#collection = db["VictimeCollection"]




client = MongoClient("mongodb://mohamed:Jackmah1998@ac-mcvyv4w-shard-00-00.juoab6m.mongodb.net:27017,ac-mcvyv4w-shard-00-01.juoab6m.mongodb.net:27017,ac-mcvyv4w-shard-00-02.juoab6m.mongodb.net:27017/?ssl=true&replicaSet=atlas-5evec0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["Victime"]
collection_auth = db["Authentification"]
collection_victim = db["VictimeCollection"]

find_email = collection_auth.find_one({
    "Username" : "mojack@gmail.com"
})

#print(find_email["Username"])


