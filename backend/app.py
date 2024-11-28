from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

quotes = [
    "asdf",
    "gogoogo",
    "hello world"
]

@app.route('/quote', methods=['GET'])
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)
