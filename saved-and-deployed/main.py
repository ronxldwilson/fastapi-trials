from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get('/')
def main():
    return {"message": "Hello from saved-and-deployed!"}

@app.post("/predict")
def predict(features: IrisInput):
    data = np.array([
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]).reshape(1, -1)

    prediction = model.predict(data)[0]
    return {"prediction": int(prediction)}

if __name__ == "__main__":
    main()
