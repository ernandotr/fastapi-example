from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: int

@app.get("/", response_model = User)
async def linuxtips():
    return User(
        name ="Ernando Rezende",
        email = "ernando.03@gmail.com",
        age = 25
    )

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}