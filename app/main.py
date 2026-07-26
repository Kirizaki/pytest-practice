from uuid import uuid4

from fastapi import FastAPI
from fastapi import HTTPException

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


@app.get("/download/{file_id}")
def download(file_id: str):
    if file_id not in files:
        raise HTTPException(status_code=404, detail="File not found")
    
    return files[file_id]

