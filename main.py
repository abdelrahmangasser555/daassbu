# simple fast api server
import uvicorn
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/docker")
def read_root():
    return {"Hello": "World"}

uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))