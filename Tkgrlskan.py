from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent


@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)