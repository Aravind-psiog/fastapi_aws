from mangum import Mangum
from fastapi import FastAPI
import os

app = FastAPI()

#
@app.get("/")
async def root():
    return {"message": "Hello from aws."}

handler = Mangum(app=app)