from fastapi import FastAPI

app = FastAPI(title="ClipAI API")

@app.get("/")
def home():
    return {
        "message": "Selamat datang di ClipAI",
        "status": "online"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
