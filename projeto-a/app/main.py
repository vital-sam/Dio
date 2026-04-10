from fastapi import FastAPI
from app.pipeline import pipeline_diario

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/run")
def run_pipeline():
    pipeline_diario()
    return {"message": "Pipeline executado com sucesso"}
