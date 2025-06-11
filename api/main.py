from fastapi import FastAPI, HTTPException
import uvicorn
import numpy as np
import pickle

# Load model and mappings
from implicit.als import AlternatingLeastSquares
import scipy.sparse as sparse

# === Load pre-trained model and data ===
# These should be saved from your notebook
model = pickle.load(open("models/als_model.pkl", "rb"))

user_item_matrix = pickle.load(open("models/user_item_matrix.pkl", "rb"))
user_mapping = pickle.load(open("models/user_mapping.pkl", "rb"))
item_mapping = pickle.load(open("models/item_mapping.pkl", "rb"))

# Reverse item mapping
reverse_item_mapping = {v: k for k, v in item_mapping.items()}


from pydantic import BaseModel

class Recommendation(BaseModel):
    item_id: int
    score: float

class RecommendationResponse(BaseModel):
    user_id: int
    recommended_items: list[Recommendation]


# === FastAPI app ===
app = FastAPI()


@app.get("/")
def root():
    return {"status": "FastAPI is working"}

@app.get("/recommendations", response_model=RecommendationResponse)
def get_recommendations(user_id: int, N: int = 5):
    if user_id not in user_mapping:
        raise HTTPException(status_code=404, detail="User ID not found")

    user_idx = user_mapping[user_id]
    try:
        recommendations = model.recommend(user_idx, user_item_matrix[user_idx], N=N)
        results = []
        for row in recommendations:
            item_idx = int(row[0])
            score = float(row[1])
            if item_idx in reverse_item_mapping:
                results.append({
                    "item_id": int(reverse_item_mapping[item_idx]),
                    "score": round(score, 4)
                })
        return {"user_id": user_id, "recommended_items": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
