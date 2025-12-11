from fastapi import FastAPI,HTTPException
import joblib
import pandas as pd
from Api.Schemas import input_data


app= FastAPI( 
            title="Credit Card Fraud Detection API",
            description="Predict fraud using Random Forest + Pipeline",
            version="1.0"
            )

#load the model

try:
    bundle = joblib.load(r"C:\Users\SK MIANUR RAHAMAN\OneDrive\Desktop\Credit Card Fraud\Credit_Card_Fraud_Detection\Model\Fraud_model_rf.pkl")
    model = bundle["model"]
    Threshold = bundle["threshold"]

except Exception as e:
    raise RuntimeError(f"Error loading model: {str(e)}")



@app.get("/")
def root():
    return {"message": "API running"}


#------------------------------------------------------
        #Prediction Endpoint
#-------------------------------------------------------
@app.post("/predict")
def predict(data : input_data):
    
    try:
        data_dict = data.model_dump()
        df = pd.DataFrame([data_dict])
        
        prob = model.predict_proba(df)[0][1]
        prediction = 1 if prob >= Threshold else 0
        
        return {
            "prediction": prediction,
            "Fraud_Probability" : float(prob),
            "ThresHold Used":float(Threshold)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))