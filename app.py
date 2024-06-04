from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bmi', methods=['GET'])
def calculate_bmi():
    weight = request.args.get('weight', type=float)
    height = request.args.get('height', type=float)
    if weight is None or height is None:
        return jsonify(error="Invalid input"), 400
    
    try:
        bmi = weight / (height ** 2)
        return jsonify(bmi=bmi)
    except (ValueError, TypeError):
        return jsonify(error="Invalid data type"), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
