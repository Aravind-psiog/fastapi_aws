from mangum import Mangum
from fastapi import FastAPI
import os

#app = FastAPI()
# only used for aws for loading Swagger doc. Doesnot work on windows
app = FastAPI(root_path="/dev/")

#


@app.get("/")
async def root():
    return {"message": "Hello from aws updated."}

handler = Mangum(app=app)
