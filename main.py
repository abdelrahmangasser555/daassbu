# simple fast api server
import uvicorn
from fastapi import FastAPI
# import necessary libraries for CORS
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/docker")
def read_root():
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    pinecone_api_key = os.environ.get("PINECONE_API_KEY")

    return {"Hello": "shorse shorse shorse", "openai_api_key": openai_api_key, "pinecone_api_key": pinecone_api_key}

uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))