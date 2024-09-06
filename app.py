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
    key = "a4562100-6c31-11ef-96ac-4d5c792cfbb3fc5ff298-681f-470c-9b37-585d0a67b1a0"
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


