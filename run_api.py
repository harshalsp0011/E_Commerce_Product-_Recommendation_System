
import subprocess

print("🚀 Starting the FastAPI recommender API...")
print("📡 Visit: http://127.0.0.1:8000/recommendations?user_id=0")
print("📘 Swagger Docs: http://localhost:8000/docs")

subprocess.run(["uvicorn", "api.main:app", "--reload"])


#python run_api.py
#uvicorn api.main:app --reload

# comand to generate requirement.txt
#pip freeze > requirements.txt

# comand to create docker image
#docker build -t recommender-api .


# comand to run docker 
#docker run -p 8000:8000 recommender-api  