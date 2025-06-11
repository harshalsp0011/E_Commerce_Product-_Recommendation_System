# 🛍️ E-Commerce Product Recommendation System

This project implements a **personalized product recommendation engine** for e-commerce users using implicit feedback data (clicks, add-to-cart, transactions). It includes:

- 🔍 EDA on event logs from RetailRocket
- 🎯 ALS collaborative filtering with the `implicit` library
- 🚀 API deployment via FastAPI + Docker
- 🖼️ Optional Streamlit UI for demo
- ✅ Full testing with curl, Swagger, and browser

---

## 🚀 Demo

📡 API Endpoint: `GET /recommendations?user_id=0&N=5`  
🧪 Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
🌐 Streamlit UI: [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

├── api/ ← FastAPI app

├── streamlit_app/ ← UI to query API

├── models/ ← Pickled ALS model

├── notebooks/ ← EDA + training

├── run_api.py ← Script to start API

├── requirements.txt ← Dependencies

├── Dockerfile ← Docker build config

├── README.md ← You are here



---

## 🧠 Key Features

- Weighted implicit event modeling: `view=1`, `addtocart=3`, `transaction=5`
- Sparse matrix modeling using ALS
- Real-time top-N recommendations for a given user
- REST API deployed via FastAPI and Docker
- Swagger documentation auto-generated
- Optional Streamlit dashboard interface

---

## 🐳 Run with Docker

```bash
# Build the image
docker build -t recommender-api .

# Run the container
docker run -p 8000:8000 recommender-api


🧪 Test the API
# Get 5 recommendations for user 0
curl "http://localhost:8000/recommendations?user_id=0&N=5"

📊 Streamlit Frontend
streamlit run streamlit_app/app.py
Visit: http://localhost:8501


📚 Dataset
RetailRocket E-Commerce Dataset on Kaggle


