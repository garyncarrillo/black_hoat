from fastapi import FastAPI, Header, HTTPException
from typing import Union, Optional
from user import User, UpdateUser
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    street: str
    phone: str

class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    street: Optional[str] = None
    phone: Optional[str] = None


users = {
}

@app.get("/users/{user_id}")
async def get_user(user_id: int = Header()):
    if user_id in users:
        return users[user_id]

    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}")
async def update_user(user_id: int = Header(), user : Union[UpdateUser, None] = None):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    if user.first_name != None:
        users[user_id].first_name = user.first_name

    if user.last_name != None:
        users[user_id].last_name = user.last_name

    if user.email != None:
        users[user_id].email = user.email

    if user.street != None:
        users[user_id].street = user.street

    if user.phone != None:
        users[user_id].phone = user.phone

    return users[user_id]

@app.delete("/users/{user_id}")
async def delete_user(user_id: int = Header()):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    del users[user_id]
    return {"Message": "User Deleted Succesfully"}

@app.get("/")
async def index():
    return users

@app.post("/users/{user_id}")
async def create_user(user_id: int = Header(), user: Union[User, None] = None):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User Already Exists")

    users[user_id] = user
    return users[user_id]
