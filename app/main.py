from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.storage import Storage

app = FastAPI()
storage = Storage()


@app.exception_handler(KeyError)
async def key_error_handler(request: Request, exc: KeyError):
    return JSONResponse(
        status_code=404,
        content={"detail":"File not found"}
    )


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail":"Storage error"}
    )


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
def upload(content: str):
    file_id = str(uuid4())

    storage.save(file_id, content)

    return { "id": file_id }


@app.get("/download/{file_id}")
def download(file_id: str):
    return { "content": storage.get(file_id) }


@app.delete("/file/{file_id}")
def delete(file_id: str):
    storage.delete(file_id)
    return {"deleted": True}

