# docker container main application file

from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def read_root():
    container_id = os.getenv("HOSTNAME", "unknown")

    return {"message": f"Hello from container {container_id}"}
