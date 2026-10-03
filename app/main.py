from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from my DevOps project"}

@app.get("/health")
def health():
    return {"status": "ok"}