# server.py
import http.server
import socketserver
import json
import random

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/play':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            user_choice = json.loads(data.decode('utf-8'))['user_choice']
            computer_choice = random.choice(['rock', 'paper', 'scissors'])
            result = determine_winner(user_choice, computer_choice)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'result': result}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'paper' and computer == 'rock') or \
       (user == 'scissors' and computer == 'paper'):
        return 'win'
    else:
        return 'lose'

if __name__ == '__main__':
    PORT = 8080
    with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
