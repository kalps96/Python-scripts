import requests
from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
  name: str
  price: float

api_url = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"
@app.get("/")
def read_root():
    return {"hello" : "books"}

@app.get("/items/{item_id}")
def get_items(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item ):
    return {"item_name": item.name, "item_id": item_id}


