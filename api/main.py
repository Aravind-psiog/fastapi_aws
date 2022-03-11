from mangum import Mangum
from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

handler = Mangum(app=app)