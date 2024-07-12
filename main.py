from fastapi import FastAPI
import requests
from pydantic import BaseModel, EmailStr
from typing import Any

app = FastAPI()

URL = "https://vsrm.dev.azure.com/vincentnd2002/Chailease/_apis/release/definitions/1?api-version=7.1-preview.4"

class variable(BaseModel):
    value: str

class Variables(BaseModel):
    appName: variable
    limits_cpu: variable
    limits_memory: variable
    requests_cpu: variable
    requests_memory: variable

class PipelineResponse(BaseModel):
    Pipeline_name: str
    Variables: Variables
    

@app.get("/callAzure/")
def get_pipeline_variable(
    organization: str = "vincentnd2002",
    project: str = "Chailease",
    definition_id: int = 1
):
    url = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions/{definition_id}?api-version=7.1-preview.4"
    response = requests.get(url).json()
    
    return response 

@app.post("/mockTest/", response_model=PipelineResponse)
def get_value(responseIn: PipelineResponse) -> Any :
    return responseIn

