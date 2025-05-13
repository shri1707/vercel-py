# api/index.py
import json
import os

# Load JSON data from file (only once)
data_file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
with open(data_file_path, "r") as f:
    STUDENT_DATA = json.load(f)

# Convert list to dict for quick lookup (optional for performance)
NAME_TO_MARKS = {entry["name"]: entry["marks"] for entry in STUDENT_DATA}

def handler(request, response):
    # Enable CORS
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    # Handle preflight (OPTIONS) request
    if request.method == "OPTIONS":
        response.status_code = 204
        return response

    # Get the query parameters
    params = request.query.get("name")
    if not params:
        names = []
    elif isinstance(params, list):
        names = params
    else:
        names = [params]

    # Retrieve marks in the same order as names
    result = [NAME_TO_MARKS.get(name, None) for name in names]

    # Send JSON response
    response.headers["Content-Type"] = "application/json"
    response.status_code = 200
    response.body = json.dumps({"marks": result})
    return response
