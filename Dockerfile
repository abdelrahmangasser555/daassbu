#FROM public.ecr.aws/docker/library/python:3.11.0-slim-bullseye
#COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.7.1 /lambda-adapter /opt/extensions/lambda-adapter
#
#ARG VAR1
#ARG VAR2
#ARG VAR3
#
#ENV OPENAI_API_KEY=$VAR1
#ENV PINECONE_API_KEY=$VAR2
#ENV GRAPHQL_API_ID=$VAR3
#
## install fagstapi and uvicorn
#RUN pip install fastapi uvicorn boto3 requests
#
#WORKDIR /app
#ADD . .
#
#CMD ["python", "main.py"]
FROM public.ecr.aws/lambda/python:3.11

ARG VAR1
ARG VAR2
ARG VAR3

ENV OPENAI_API_KEY=$VAR1
ENV PINECONE_API_KEY=$VAR2
ENV GRAPHQL_API_ID=$VAR3

RUN pip install fastapi uvicorn boto3 requests

COPY . ${LAMBDA_TASK_ROOT}

CMD [ "handler.lambda_handler" ]