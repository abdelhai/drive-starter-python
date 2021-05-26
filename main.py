from fastapi import FastAPI, File, UploadFile, responses
from deta import Drive

app = FastAPI()
files = Drive("files")


@app.post("/")
def upload(file: UploadFile = File(...)):
    return files.put(file.filename, file.file)


@app.get("/")
def list_files():
    return files.list()


@app.get("/{name}")
def serve(name):
    img = files.get(name)
    ext = name.split(".")[1]
    return responses.StreamingResponse(img.iter_chunks(), media_type=f"image/{ext}")
