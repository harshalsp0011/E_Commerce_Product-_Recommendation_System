# 🛍️ E-Commerce Product Recommendation System

A **scalable, end-to-end recommendation engine** delivering personalized product suggestions for e-commerce users using implicit feedback data (clicks, add-to-cart events, purchases) from RetailRocket's clickstream dataset.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green.svg)]
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)]

---

## 🚀 Demo

- **API Endpoint**: `GET /recommendations?user_id=17&N=5`
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Streamlit Dashboard**: [http://localhost:8501](http://localhost:8501)

---

## 🔑 Key Features

- **Implicit Feedback Modeling**: Weighted event scoring (`view=1`, `addtocart=3`, `transaction=5`)
- **ALS Collaborative Filtering**: Matrix factorization using the `implicit` library
- **High-Performance API**: Sub-200ms response times with FastAPI
- **Containerized Deployment**: Docker configuration for reproducible builds
- **Interactive Dashboard**: Streamlit UI for real-time testing
- **Cloud Ready**: Deployed on AWS EC2
- **Scalable**: Handles 2.7M+ interactions

---

## 📁 Project Structure

```
E_Commerce_Product-_Recommendation_System/
├── api/
│   ├── __pycache__/
│   │   └── main.cpython-310.pyc
│   └── main.py
├── models/
│   ├── .DS_Store
│   ├── .gitattributes
│   ├── als_model.joblib
│   ├── als_model.zip
│   ├── item_mapping.joblib
│   ├── item_mapping.zip
│   ├── user_item_matrix.joblib
│   ├── user_item_matrix.zip
│   ├── user_mapping.joblib
│   └── user_mapping.zip
├── notebooks/
│   └── 01_eda.ipynb
├── streamlit_app/
│   └── app.py
├── venv/
│   ├── bin/
│   ├── lib/
│   ├── share/
│   ├── .DS_Store
│   └── pyvenv.cfg
├── Visuals/
│   ├── API TESTING A.png
│   ├── API.png
│   ├── Postman chekcing.png
│   ├── Process.png
│   ├── Streatlit application.png
│   └── matrix.png
├── .DS_Store
├── Dockerfile
├── README.md
├── requirements.txt
└── run_api.py
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/your-username/E_Commerce_Product-_Recommendation_System.git
cd E_Commerce_Product-_Recommendation_System

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
``` 

### Run API

```bash
# Direct start
python run_api.py

# Uvicorn
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

### Launch Dashboard

```bash
streamlit run streamlit_app/app.py
``` 

### Docker

```bash
docker build -t recommender-api .
docker run -p 8000:8000 recommender-api
``` 

---

## 📡 API Reference

### Get Recommendations
```
GET /recommendations?user_id={USER_ID}&N={TOP_N}
```
**Parameters:**
- `user_id` (integer, required): Visitor ID
- `N` (integer, optional): Number of recommendations (default: 5)

**Response:**
```json
{
  "user_id": 17,
  "recommended_items": [
    {"item_id": 67818, "score": 892013.0},
    {"item_id": 67045, "score": 0.0}
  ]
}
```

### Get Users
```
GET /users
```
**Response:**
```json
{
  "total_users": 1407580,
  "sample_user_ids": [0,1,2,3,4]
}
```

---

## 🧠 Model & Pipeline

- **Data Ingestion**: RetailRocket event logs
- **Preprocessing**: Map events to strengths & build sparse matrix
- **ALS Training**: factors=50, reg=0.01, iter=15
- **Serialization**: Joblib for model and mappings

---

## 📊 Visuals

Screenshots and diagrams are available in the `Visuals/` folder.

---

## 🧪 Testing

```bash
# Manual API test
curl "http://localhost:8000/recommendations?user_id=17&N=5"

# Unit tests
pytest -v

# Load testing
ab -n 500 -c 10 "http://localhost:8000/recommendations?user_id=17&N=5"
```
