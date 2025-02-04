from fastapi import FastAPI, Form
from pydantic import BaseModel
import joblib
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

class InputData(BaseModel):
    input1: float
    input2: int
    input3: int
    
# define model
model = joblib.load("LinearModel.pkl")

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
        input_values = [[input1, input2, input3]]
        prediction = model.predict(input_values)[0]
        return {"fuel consumption prediction": prediction}
    except Exception as e:
        return {"error": str(e)}