from mangum import Mangum
from fastapi import FastAPI
import os

#app = FastAPI()
app = FastAPI(root_path="/dev/") #only used for aws for loading Swagger doc. Doesnot work on windows

#
@app.get("/")
async def root():
    return {"message": "Hello from aws."}

handler = Mangum(app=app)