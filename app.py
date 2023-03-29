from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
marks = {
    "name": "Jasteg Singh",
    "roll_no": "21cs2008",
    "subjects": {
        "Web Technology": 80,
        "DBMS": 90,
        "COA": 96
    }
}

# API to get marks data
@app.route('/marks', methods=['GET'])
def get_marks():
    return jsonify(marks)

# API to update marks data
@app.route('/marks', methods=['PUT'])
def update_marks():
    req_data = request.get_json()
    for subject, mark in req_data.items():
        marks["subjects"][subject] = mark
    return jsonify(marks)

# API to delete marks data
@app.route('/marks', methods=['DELETE'])
def delete_marks():
    marks["subjects"] = {}
    return jsonify(marks)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
