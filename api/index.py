import json

# Hardcoded student data
students = [
    {"name": "d", "marks": 27},
    {"name": "C6xuo", "marks": 88},
    {"name": "96ZTC7rsE", "marks": 40},
    {"name": "t", "marks": 85},
    {"name": "yW2y", "marks": 87},
    {"name": "00", "marks": 36},
    {"name": "jm7bQ", "marks": 77},
    {"name": "TpZ1ltLJ0", "marks": 20},
    {"name": "7lWVCbb04", "marks": 73},
    {"name": "UZTaBGVkeb", "marks": 6},
    {"name": "omI", "marks": 6},
    {"name": "aj9LY8x", "marks": 35},
    {"name": "L4FLUbCeR3", "marks": 54},
    {"name": "yxDUSOi", "marks": 83},
    {"name": "DYvVj", "marks": 29},
    {"name": "JS", "marks": 13},
    {"name": "lsTB", "marks": 5},
    {"name": "m", "marks": 15},
    {"name": "P", "marks": 13},
    {"name": "ATgsmS", "marks": 76},
    {"name": "ETJD", "marks": 67},
    {"name": "rj3", "marks": 94},
    {"name": "uICR69", "marks": 20},
    {"name": "7wa", "marks": 29},
    {"name": "nj7md", "marks": 16},
    {"name": "DjoW", "marks": 59},
    {"name": "ybRCDk1Plt", "marks": 64},
    {"name": "onv2G6uW", "marks": 59},
    {"name": "pG4b8E", "marks": 62},
    {"name": "iCX", "marks": 28},
    {"name": "qvcPn4r67i", "marks": 96},
    {"name": "6uTkfK6a", "marks": 41},
    {"name": "E", "marks": 97},
    {"name": "HQRhU2t", "marks": 86},
    {"name": "8", "marks": 91},
    {"name": "l8RmXj", "marks": 76},
    {"name": "RH7Pe9SsY", "marks": 69},
    {"name": "Xu", "marks": 70},
    {"name": "T", "marks": 27},
    {"name": "Kw0J", "marks": 98},
    {"name": "G", "marks": 25},
    {"name": "KEIF", "marks": 39},
    {"name": "0aqE", "marks": 57},
    {"name": "u4t72", "marks": 45},
    {"name": "O3ojXRO", "marks": 87},
    {"name": "lCgn", "marks": 99},
    {"name": "nk7UX39Q", "marks": 52},
    {"name": "WqP6niuJCb", "marks": 78},
    {"name": "CEwcO5", "marks": 26},
    {"name": "OdRM8E", "marks": 19},
    {"name": "5", "marks": 53},
    {"name": "GehdLAeb", "marks": 31},
    {"name": "bEV", "marks": 21},
    {"name": "VEWp", "marks": 1},
    {"name": "GYN", "marks": 34},
    {"name": "OCkVzudx", "marks": 97},
    {"name": "8QzRGDV", "marks": 87},
    {"name": "xHy", "marks": 7},
    {"name": "q97sp", "marks": 52},
    {"name": "o31sNOX", "marks": 42},
    {"name": "6s1kQXq", "marks": 94},
    {"name": "5p", "marks": 93},
    {"name": "eSeVx", "marks": 41},
    {"name": "aQDb", "marks": 19},
    {"name": "izPb2vrPL", "marks": 0},
    {"name": "k5qZNIp2qz", "marks": 96},
    {"name": "Ldn", "marks": 69},
    {"name": "08kq", "marks": 93},
    {"name": "6va", "marks": 55},
    {"name": "j", "marks": 4},
    {"name": "pBpc", "marks": 31},
    {"name": "HMhdjRxO1d", "marks": 77},
    {"name": "1Q33HIc7", "marks": 64},
    {"name": "S", "marks": 88},
    {"name": "S3", "marks": 53},
    {"name": "5FBW8", "marks": 55},
    {"name": "uZEVtEG4", "marks": 73},
    {"name": "yVNjG0PBU", "marks": 21},
    {"name": "AB88hQDFd", "marks": 51},
    {"name": "8XV", "marks": 66},
    {"name": "fa", "marks": 58},
    {"name": "GCkb7j30", "marks": 91},
    {"name": "uvW4L", "marks": 57},
    {"name": "sWzIYOgC", "marks": 6},
    {"name": "saWLI", "marks": 76},
    {"name": "8LW", "marks": 51},
    {"name": "779Q", "marks": 19},
    {"name": "cENaUXm", "marks": 14},
    {"name": "CAgH6", "marks": 13},
    {"name": "ccfb0G", "marks": 24},
    {"name": "pGrI", "marks": 70},
    {"name": "nfX", "marks": 48},
    {"name": "qn5n", "marks": 74},
    {"name": "iv", "marks": 20},
    {"name": "iJk", "marks": 46},
    {"name": "i7s4I9cm", "marks": 60},
    {"name": "YCJU", "marks": 28},
    {"name": "pL", "marks": 14},
    {"name": "9bq", "marks": 96},
    {"name": "TlwU", "marks": 57}
]

# Create lookup dictionary
student_lookup = {entry["name"]: entry["marks"] for entry in students}

def handler(request, response):
    # Enable CORS
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
