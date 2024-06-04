from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/bmi')
def calculate_bmi():
    data = request.get_json()
    height = float(data['height'])
    weight = float(data['weight'])
    bmi = weight / (height ** 2)
    return jsonify(bmi=bmi)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
