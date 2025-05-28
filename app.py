from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/buy', methods=['POST'])
def buy():
    data = request.json
    print(f"Покупка: {data['item']}")
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True)
