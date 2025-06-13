import requests
from fastapi import FastAPI, Path
app = FastAPI()

api_url = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"
@app.get("/")
def read_root("/"):
    return {"hello" : "books"}

@app.get("/items")
def get_items(item_id: int):
    return {"item_id": item_id}


