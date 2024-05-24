import os
import boto3
import asyncio
import requests
import json
import time

def lambda_handler(event, context):

    graphql_url = event["graphql_url"]
    authorization = event["auth"]

    query = "mutation ($input: CreateTodoInput!) {\n  createTodo(input: $input) {\n    id\n    content\n    createdAt\n    updatedAt\n  }\n}\n"

    time.sleep(20)

    for i in range(10):
        variables = {"input": {"content": f"Hello, World! {i}"}}
        payload = {"query": query, "variables": variables}

        headers = {
            'Content-Type': 'application/json',
            'Authorization': authorization
        }

        response = requests.post(graphql_url, headers=headers, data=json.dumps(payload))

        # sleep for 2 seconds
        time.sleep(3)

    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }
    # openai_api_key = os.environ.get("OPENAI_API_KEY")
    # pinecone_api_key = os.environ.get("PINECONE_API_KEY")
    # graphql_api_id = os.environ.get("GRAPHQL_API_ID")
    #
    # client = boto3.client('appsync')
    #
    # r = client.get_graphql_api(apiId=graphql_api_id)
    #
    # graphql_url = r['graphqlApi']['uris']['GRAPHQL']
    #
    # authorization = request.headers.get("Authorization")
    #
    # query = "mutation ($input: CreateTodoInput!) {\n  createTodo(input: $input) {\n    id\n    content\n    createdAt\n    updatedAt\n  }\n}\n"
    #
    # for i in range(10):
    #     variables = {"input": {"content": f"Hello, World! {i}"}}
    #     payload = {"query": query, "variables": variables}
    #
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'Authorization': authorization
    #     }
    #
    #     response = requests.post(graphql_url, headers=headers, data=json.dumps(payload))
    #
    #     # sleep for 2 seconds
    #     asyncio.sleep(2)