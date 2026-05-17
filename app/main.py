from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base
from app.db import models

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None):
    return {"item_id": item_id, "q": q}
