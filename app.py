from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешение запросов с любых источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешение всех методов (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешение всех заголовков
)

class TextRequest(BaseModel):
    text: str


@app.post("/classify")
async def classify(request: TextRequest):
    key = ("50bba060-6a56-11ef-b807-b1c86b00d51ab2f4b0dd-64aa-430e-983f"
           "-cf9fcf6cc4eb")
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


