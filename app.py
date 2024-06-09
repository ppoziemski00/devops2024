from flask import Flask, request, jsonify, send_from_directory
import webbrowser
import threading
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_index():
    index_path = os.path.join(app.static_folder, 'index.html')
    print(f"Serving index.html from {index_path}")
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/bmi', methods=['POST'])
def calculate_bmi():
    data = request.get_json()
    if not data or 'height' not in data or 'weight' not in data:
        return jsonify(error="Invalid input"), 400
    
    try:
        height = float(data['height']) / 100
        weight = float(data['weight'])
        bmi = weight / (height ** 2)
        return jsonify(bmi=bmi)
    except (ValueError, TypeError):
        return jsonify(error="Invalid data type"), 400

def open_browser():
    webbrowser.open_new('http://localhost:5000/')

if __name__ == '__main__':
    index_path = os.path.join(app.static_folder, 'index.html')
    if os.path.exists(index_path):
        print(f"index.html found at {index_path}")
    else:
        print(f"index.html not found at {index_path}")

    threading.Timer(1.25, open_browser).start()
    app.run(host='0.0.0.0', port=5000)
