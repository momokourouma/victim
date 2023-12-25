import pydantic
import uvicorn
from fastapi import FastAPI, Body
from bson.objectid import ObjectId
from starlette.middleware.cors import CORSMiddleware
from ModelVictime import VictimeModel, UpdateVictim, Authentification
from DatabaseConnection import collection_auth
from HashingPassword import hashingPassword
from DatabaseConnection import collection_victim
from UserValidation import Validation

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/v1/add/admin")
async def addAdmin(admin: Authentification = Body(...)):
    hash_password = hashingPassword(admin.password)
    user_name = admin.email
    admin.password = hash_password
    print(user_name)

    new_user = collection_auth.find_one({"email": admin.email})
    if new_user:
        return {"utilisateur existe deja"}
    else:
        new_admin = collection_auth.insert_one(admin.dict())
        return {"info": "Adminstrsteur cree avec success"}


@app.post("/v1/auth/admin")
async def Authadmin(authAdmin: Validation = Body(...)):
    admin_email = authAdmin.email
    admin_password = hashingPassword(authAdmin.password)

    finding_password = await collection_auth.find_one({
        "email": admin_email
    })

    finding_email = await collection_auth.find_one({
        "password": admin_password
    })

    if (finding_password["password"] != admin_password):
        return {"info": "Mot de passe invalid"}

    elif (finding_email["email"] != admin_email):
        return {"info": "Email incorrect"}

    else:
        return {"info": "success"}


@app.get("/v1/auth/information")
async def auth_info():
    auth_user: list = []
    for x in collection_auth.find({}, {"password": 0}):
        auth_user.append(x)
    return auth_user


@app.post("/v1/add/victim")
async def AddVictim(victim: VictimeModel = Body(...)):
    new_victim = collection_victim.insert_one(victim.dict())
    my_id = str(new_victim.inserted_id)
    return victim


@app.put("/v1/update/victim/{victim_id}")
async def UpdateVictim(victim_id: str, victim: UpdateVictim = Body(...)):
    ObjectId(victim_id.strip("''"))
    victim = {k: v for k, v in victim.dict().items() if v is not None}
    find_c = collection_victim.find_one_and_update({"_id": ObjectId(victim_id.strip("''"))}, {"$set": victim})
    if find_c is not None:
        return {"info": "modifier avec suc"}
    else:
        return {"info": " erreur de mofi"}


@app.delete("/v1/delete/victim/{victim_id}")
async def DeleteVictim(victim_id: str):
    ObjectId(victim_id.strip("''"))
    delete_victim = collection_victim.delete_one({"_id": ObjectId(victim_id.strip("''"))})
    print(victim_id)
    if delete_victim.deleted_count == 1:
        return "success"


@app.delete("/v1/delete/user/{user_id}")
async def DeleteUser(user_id: str):
    ObjectId(user_id.strip("''"))
    delete_victim = collection_auth.delete_one({"_id": ObjectId(user_id.strip("''"))})
    if delete_victim.deleted_count == 1:
        return "success"


@app.get("/v1/get/information/victim")
async def getinfo():
    victim_info: list = []
    for x in collection_victim.find():
        victim_info.append(x)

    return victim_info


@app.get("/v1/get/valid/victim")
async def getTrueVictim():
    victim_info: list = []
    for x in collection_victim.find({"statut": True}):
        victim_info.append(x)

    return victim_info


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
