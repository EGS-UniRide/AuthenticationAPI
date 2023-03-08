from fastapi import FastAPI
from pydantic import BaseModel

class Auth(BaseModel):
    authid: str
    token: str
    date: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/login")
async def all_auth():
    return users

@app.get("/authetication/{authid}")
async def get_auth(authid: str):
    if authid in users:
        return users[authid]
    else:
        return {"Authentication not found"}
    
@app.post("/authentication")
async def post_auth(auth: Auth):
    users[auth.authid] = auth
    return auth

@app.delete("/authentication/{authid}")
async def del_auth(authid: str):
    if authid in users:
        users.pop(authid)
        return {"Authentication deleted successfully"}
    else:
        return {"Authentication not found"}
    
@app.put("/authentication/{authid}")
async def put_auth(authid: str, auth: Auth):
    if authid in users:
        users[authid] = auth
        return {"Authentication list updated successfully"}
    else:
        return {"Authentication not found"}