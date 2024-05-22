# simple fast api server
import uvicorn
from fastapi import FastAPI, Request
# import necessary libraries for CORS
from fastapi.middleware.cors import CORSMiddleware
import os
import boto3
import asyncio
import requests
import json

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
def read_root(request: Request):
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    pinecone_api_key = os.environ.get("PINECONE_API_KEY")
    graphql_api_id = os.environ.get("GRAPHQL_API_ID")

    client = boto3.client('appsync')

    r = client.get_graphql_api(apiId=graphql_api_id)

    graphql_url = r['graphqlApi']['uris']['GRAPHQL']

    authorization = request.headers.get("Authorization")

    query = "mutation ($input: CreateTodoInput!) {\n  createTodo(input: $input) {\n    id\n    content\n    createdAt\n    updatedAt\n  }\n}\n"

    for i in range(10):
        variables = {"input": {"content": f"Hello, World! {i}"}}
        payload = {"query": query, "variables": variables}

        headers = {
            'Content-Type': 'application/json',
            'Authorization': authorization
        }

        response = requests.post(graphql_url, headers=headers, data=json.dumps(payload))

        # sleep for 2 seconds
        asyncio.sleep(2)

    return {"Hello": "shorse shorse very shorse", "openai_api_key": openai_api_key, "pinecone_api_key": pinecone_api_key, "graphql_api_id": graphql_api_id}

uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))