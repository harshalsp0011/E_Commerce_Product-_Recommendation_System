
import subprocess

print("🚀 Starting the FastAPI recommender API...")
print("📡 Visit: http://127.0.0.1:8000/recommendations?user_id=0")
print("📘 Swagger Docs: http://127.0.0.1:8000/docs\n")

subprocess.run(["uvicorn", "api.main:app", "--reload"])


#python run_api.py
#uvicorn api.main:app --reload
