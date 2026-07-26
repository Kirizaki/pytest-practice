from uuid import uuid4

from fastapi import FastAPI

app = FastAPI()

files = {}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
def upload(content: str):
    file_id = str(uuid4())

    files[file_id] = {
        "content": content
    }

    return { "id": file_id }

