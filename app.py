from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import requests

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

if __name__ == 'main':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)


# CHANGE THIS to something you want your machine learning model to classify

