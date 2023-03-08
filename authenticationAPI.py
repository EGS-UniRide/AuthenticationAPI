from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class Auth(BaseModel):
    authid: str
    token: str
    date: datetime

app = FastAPI()

auths={}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/v1/authetications")
async def all_auth():
    return auths

@app.get("/v1/authetications/{authid}")
async def get_auth(authid: str):
    if authid in auths:
        return auths[authid]
    else:
        return {"404: Authentication not found"}
    
@app.post("/v1/authentications")
async def post_auth(auth: Auth):
    auths[auth.authid] = auth
    return auth

@app.delete("/v1/authentications/{authid}")
async def del_auth(authid: str):
    if authid in auths:
        auths.pop(authid)
        return {"200: Authentication deleted successfully"}
    else:
        return {"404: Authentication not found"}
    
@app.put("/v1/authentications/{authid}")
async def put_auth(authid: str, auth: Auth):  ##mudar para update
    if authid in auths:
        auths[authid] = auth
        return {"200: Authentication list updated successfully"}
    else:
        return {"404: Authentication not found"}

@app.put("/v1/authentications/register")
async def put_register(authid: str):        #a date seria a do momento e o token seria gerado?
    if authid in auths:
        return { "40: User id already exists"}
    else:
        date = datetime.now()