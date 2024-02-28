from typing import Optional

from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello GUYS!"}

@app.get("/test")
async def test():
    return {"message": "This is a test"}

@app.post("/add_person")
def add_person(age: int, income: int):
    data = {"age": age, "income": income}
    df = pd.read_csv("db.csv")
    df = pd.concat([df, pd.DataFrame([data])])
    df.to_csv("db.csv", index=False)
    return df.to_dict('records')

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
