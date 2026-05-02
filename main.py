from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = joblib.load("spam_model.pkl")

class MessageRequest(BaseModel):
    message: str

@app.post("/predict")
def predict(data: MessageRequest):
    message = data.message

   
    prediction = model.predict([message])[0]
    probs = model.predict_proba([message])[0]

   
    tfidf = model.named_steps["tfidf"]
    classifier = model.named_steps["classifier"]

   
    X_tfidf = tfidf.transform([message])

  
    feature_names = tfidf.get_feature_names_out()
    weights = classifier.coef_[0]

    
    indices = X_tfidf.nonzero()[1]

    
    top_indices = sorted(indices, key=lambda i: weights[i], reverse=True)[:5]

    keywords = [feature_names[i] for i in top_indices]

    return {
        "label": "spam" if prediction == 1 else "ham",
        "confidence": float(probs[1]) if prediction == 1 else float(probs[0]),
        "keywords": keywords
    }