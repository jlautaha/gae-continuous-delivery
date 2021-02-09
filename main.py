from flask import Flask
from flask import jsonify
import random
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! CD'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
