from fastapi import FastAPI
import pickle

app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Voice AI Running"}

@app.post("/predict")
def predict(text: str):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return {"intent": prediction}