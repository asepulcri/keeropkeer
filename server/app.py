from flask import Flask
from server.main import generate_board

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/get-board', methods=['GET'])
def get_board():
    return generate_board()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

