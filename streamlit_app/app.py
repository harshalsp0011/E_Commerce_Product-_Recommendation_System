# streamlit_app/app.py

import streamlit as st
import requests

st.set_page_config(page_title="E-Commerce Recommender", layout="centered")

st.title("🛍️ Product Recommendation Engine")
st.write("Enter a user ID to get personalized product recommendations.")

# Input form
user_id = st.number_input("User ID", min_value=0, step=1)
num_recs = st.slider("Number of Recommendations", min_value=1, max_value=25, value=5)

if st.button("Get Recommendations"):
    url = f"http://localhost:8000/recommendations?user_id={user_id}&N={num_recs}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            st.success(f"Top {num_recs} Recommendations for User {user_id}")
            for item in data["recommended_items"]:
                st.write(f"📦 **Item ID:** `{item['item_id']}` — Score: `{item['score']}`")
        else:
            st.error(f"❌ Error: {response.json()['detail']}")
    except Exception as e:
        st.error(f"⚠️ Could not connect to API: {e}")
