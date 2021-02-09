
from flask import Flask
from flask import jsonify
import random
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! CD'

@app.route('/coinflip/<choice>')
def coinflip(choice)
    x = random.choice(['heads','tails'])
    if choice.lower() != 'heads' and choice.lower() != 'tails':
        return 'Not a valid choice.'
    if choice.lower() == x:
        return f'You chose {choice} and you won!'
    else:
        return f'You chose {choice} and you lost!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
