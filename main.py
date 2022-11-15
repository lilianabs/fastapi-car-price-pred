import uvicorn
import joblib
import pandas as pd

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Predict": "Ford Car Price"}

@app.get("/predict")
def predict(model: str, year: int, 
            transmission: str, mileage: int,
            fuelType: str, mpg: float,
            engineSize: float
            ):
    
    model_pkl_file = "model/model_rf.pkl"
    model_rf = joblib.load(model_pkl_file)
    
    # Select the features the current model expects
    input_data = pd.DataFrame([[year, fuelType, engineSize]], 
                              columns=['year', 'fuelType', 'engineSize'])
    
    prediction = model_rf.predict(input_data)
    
    # Round the prediction
    prediction = round(prediction[0], 3)
    
    return {"Car price suggested": prediction}

if __name__ == '__main__':
    uvicorn.run(app)
    
    