from fastapi import FastAPI, Body
from typing import Union,Optional
from pydantic import BaseModel

class Item(BaseModel):
    item_id: Union[int, str]
    item_name: str
    item_bool: bool

class ItemDetail(BaseModel):
    item_color: str
    item_detail: str


app = FastAPI()

@app.get("/")
def root():
    return {"msg": "welcome to root page"}

@app.get("/items/{item_id}/{item_name}")
def show_item(item_id: int, item_name: str):
    return {"msg": f"{item_id} and {item_name}"}

@app.post("/items", status_code=201)
def create_item():
    return {"msg": "created"}

@app.get("/items")
def query_item(item_id:int=0, item_name:str=" ", item_bool:Optional[bool]=False):
    if item_bool:
        return {"item_id": item_id, "item_name": item_name}
    return {"item_id": item_id, "item_name": item_name, "item_bool": item_bool}

@app.get("/items/with_body_params")
def show_item_body_with_query(item: Item, item_color:str=Body(())):
    return {"items": item, "item_color": item_color}

@app.get("/items/combine/{item_id}")
def combine_all_params(item_id:str,item_name:str,item_detail:ItemDetail):
    return {"item_id": item_id, "item_name": item_name, "item_detail": item_detail}

