#backend.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask (__name__)
CORS(app)  #This will enable CORS for all routes

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json['choice']
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    if user_choice == computer_choice:
        result = 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissor' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = 'user'
    else:
        result = 'computer'
    return jsonify({'result': result, 'computer_choice': computer_choice})

if __name__ == '__main__':
    app.run(debug=True)