from fastapi import FastAPI, Form, HTTPException
from pydantic import BaseModel
import joblib
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd

class InputData(BaseModel):
    input1: float
    input2: int
    input3: int
    
# define model
model = joblib.load("LinearModel.pkl")

# Define valid input ranges
min_engine_size, max_engine_size = 1.0,8.0
min_cylinders, max_cylinders = 3,12
min_co2_emissions, max_co2_emissions = 104,582

# Instantiate App
app = FastAPI()

# Mount static files folder to serve HTML, CSS, JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Root endpoint serving custom UI
@app.get("/", response_class=HTMLResponse)
def root():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

# post operation 
@app.post("/predict/")
def predict(input1: float = Form(...), input2: int = Form(...), input3: int = Form(...)):
    try:
        # Validate Input Range
        if not(min_engine_size <= input1 <= max_engine_size):
            raise HTTPException(status_code=400, detail=f"Engine size must be between {min_engine_size} and {max_engine_size}.")
        if not(min_cylinders <= input2 <= max_cylinders):
            raise HTTPException(status_code=400, detail=f"Cylinders must be between {min_cylinders} and {max_cylinders}.")
        if not(min_co2_emissions <= input3 <= max_co2_emissions):
            raise HTTPException(status_code=400, detail=f"CO2 emissions must be between {min_co2_emissions} and {max_co2_emissions}.")
        
        # Make Prediction
        # Convert input to DataFrame with correct column names
        input_df = pd.DataFrame([[input1, input2, input3]], columns=["Engine size","Cylinders","Coemissions "])
        # Make Prediction
        prediction = model.predict(input_df)[0]
        
        return {"fuel_consumption_prediction": round(prediction,2)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))