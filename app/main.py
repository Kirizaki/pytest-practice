from uuid import uuid4

from fastapi import FastAPI
from fastapi import HTTPException

from app.storage import Storage

app = FastAPI()
storage = Storage()


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
def upload(content: str):
    file_id = str(uuid4())

    storage.save(file_id, content)

    return { "id": file_id }


def raise_file_not_found():
    raise HTTPException(status_code=404, detail="File not found")


@app.get("/download/{file_id}")
def download(file_id: str):
    file = storage.get(file_id)
    if file is None:
        raise_file_not_found()
    
    return { "content": file}


@app.delete("/file/{file_id}")
def delete(file_id: str):
    file = storage.get(file_id)
    if file is None:
        raise_file_not_found()
    
    storage.delete(file_id)

    return {"deleted": True}

