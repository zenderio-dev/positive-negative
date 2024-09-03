from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class TextRequest(BaseModel):
    text: str


@app.post("/classify")
async def classify(request: TextRequest):
    key = ("7f6553b0-6a11-11ef-8862-7949966a810c73b14882-3ea6-43e6-bab2"
           "-7a55915ea65c")
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={"data": request.text})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]

        return topMatch
    else:
        raise HTTPException(status_code=response.status_code, detail="Error connecting to the ML service")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the classification API"}


# CHANGE THIS to something you want your machine learning model to classify

