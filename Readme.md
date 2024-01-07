# House Price Analysis - Machine Learning Process
This repository was created to explain how to use the app. 

## Installation
Installation can be executed by running the command `docker-compose up -d`. But dont forget to install docker and docker compose.

## How to use
You can access web service using `http://localhost:8501/` and if you only want to use the endpoint, you can access `http://localhost:8000/predict/` with POST protocol and body with detail below
```
{
    "SquareFeet" : 0.1, 
    "Bedrooms" : 5.0, 
    "Bathrooms" : 2.0, 
    "YearBuilt" : 2000,
    "Neighborhood_Rural": 0, 
    "Neighborhood_Suburb" : 1,
    "Neighborhood_Urban" :1
}
```
with detail for each feature below
```
    SquareFeet: float
    Bedrooms: float
    Bathrooms: float
    YearBuilt: float
    Neighborhood_Rural: int
    Neighborhood_Suburb: int
    Neighborhood_Urban: int
```

## What's next ?
* CICD
* Deploy to server