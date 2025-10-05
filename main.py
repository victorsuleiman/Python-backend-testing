from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Items API")

class Item(BaseModel):
    id: int
    name: str

DB: dict[int, Item] = {}

@app.get("/items")
def list_items():
    return list(DB.values())

@app.post("/items", status_code=201)
def create_item(item: Item):
    if item.id in DB:
        raise HTTPException(status_code=409, detail="Item exists")
    DB[item.id] = item
    return item

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Not found")
    return DB[item_id]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Not found")
    DB[item_id] = item
    return item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in DB:
        raise HTTPException(status_code=404, detail="Not found")
    del DB[item_id] 
