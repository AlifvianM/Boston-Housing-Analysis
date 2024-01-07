import pandas as pd
import pickle
import json

from fastapi import FastAPI
from pydantic import BaseModel

class HouseData(BaseModel):
    SquareFeet: float
    Bedrooms: float
    Bathrooms: float
    YearBuilt: float
    Neighborhood_Rural: int
    Neighborhood_Suburb: int
    Neighborhood_Urban: int

app = FastAPI()

@app.get('/')
def read_root():
    return {"hello":"world"}

@app.post('/predict')
def predict(house: HouseData):
    
    data = json.loads(house.json())
    df = pd.DataFrame(data, index=[0])

    # load scaler
    with open('./model/scaler_model.pkl', 'rb') as file:
        scaler = pickle.load(file)
    
    scaled_data = scaler.transform(df)
    
    with open('./model/housing_price_model.pkl', "rb") as mod:
        loaded_lgb_model = pickle.load(mod)

    print(loaded_lgb_model)
    
    predict = loaded_lgb_model.predict(scaled_data)
    print(predict)

    return {
        "data":house,
        "predicted_price":predict[0],
        "code": "200",
        "status": "OK"
    }