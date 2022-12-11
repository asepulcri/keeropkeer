from flask import Flask, jsonify
from flask_cors import CORS
from server.main import generate_board

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/hello', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/get-board', methods=['GET'])
def get_board():
    response = jsonify(generate_board())
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

