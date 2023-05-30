from fastapi import FastAPI, Request
from joblib import load
import json
from pydantic import BaseModel
import pandas as pd


app = FastAPI()
class Prediction(BaseModel):
    age: str
    irritable_towards_baby_and_partner: str
    feeling_of_guilt: str
    problems_of_bonding_with_baby: str
    suicide_attempt: str

@app.get("/")
async def root():
    return {"message": "Running api"}

@app.post("/predict")
async def predict(data: Prediction):
    model = load('modelo_post_natal.joblib')
    return {"result": model.predict(json.loads(process_request(data)))}

def process_request(request):
    return json.dumps(request, default=lambda x: x.__dict__)