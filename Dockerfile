FROM public.ecr.aws/docker/library/python:3.11.0-slim-bullseye
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.7.1 /lambda-adapter /opt/extensions/lambda-adapter

ARG VAR1
ARG VAR2

ENV OPENAI_API_KEY=$VAR1
ENV PINECONE_API_KEY=$VAR2

# install fastapi and uvicorn
RUN pip install fastapi uvicorn

WORKDIR /app
ADD . .

CMD ["python", "main.py"]