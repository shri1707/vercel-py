# api/index.py
import json
import os

# Load JSON data from file (only once)
data_file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
with open(data_file_path, "r") as f:
    STUDENT_MARKS = json.load(f)

def handler(request, response):
    params = request.query.get("name")
    names = params if isinstance(params, list) else [params]
    result = [STUDENT_MARKS.get(name, None) for name in names]
    
    response.headers["Content-Type"] = "application/json"
    response.status_code = 200
    response.body = json.dumps({"marks": result})
    return response
