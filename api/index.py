# api/index.py
import json
import os

try:
    file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
    with open(file_path, "r") as f:
        students = json.load(f)
    student_lookup = {entry["name"]: entry["marks"] for entry in students}
except Exception as e:
    student_lookup = {}
    print("Failed to load student data:", e)

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    if request.method == "OPTIONS":
        response.status_code = 204
        return response

    query = request.query.get("name")
    names = query if isinstance(query, list) else [query] if query else []

    marks = [student_lookup.get(name, None) for name in names]

    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    response.body = json.dumps({"marks": marks})
    return response
