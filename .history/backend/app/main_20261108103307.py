from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str 
    price: float

@app.post('/items/')
def create_item(item: Item):
    return {"name": item.name, "price": item.price}

@app.get('/items/')
def get_item(item: Item):
    return {"name": item.name, "price": item.price}