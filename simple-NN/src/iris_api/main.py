from fastapi import FastAPI
from pydantic import BaseModel
from iris_api.model import predict

app = FastAPI()

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get('/')
def home():
    return {"message": "Welcome to the Iris API"}


@app.post('/predict')
def predict_iris(input: IrisInput):
    features = [input.sepal_length, input.sepal_width, input.petal_length, input.petal_width]
    result = predict(features)
    
    return {"Predicted_class": result}