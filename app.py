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
    key = "b5eff620-70d2-11ef-80ba-0f1cb52b74c46a35e727-e33c-4d28-ad2d-4d7b658cad9a"
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


