import os
from flask import Flask, jsonify
from flask_cors import CORS
from main import generate_board

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return "Hello World!"

@app.route('/hello', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/get-board', methods=['GET'])
def get_board():
    response = jsonify(generate_board())
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= int(os.environ.get('PORT', 8000)))

