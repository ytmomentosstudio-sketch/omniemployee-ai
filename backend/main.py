from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OmniEmployee AI Backend Running 🚀"}