from flask import Flask 
import socket, json

app = Flask(__name__)

@app.route('/')
def print_ip():
    hostname = socket.gethostname()
    get_ip = socket.gethostbyname(hostname)
    return get_ip

@app.route('/health')
def check_health():
    return json.dumps({'success':True}, 200, {'contentType': 'application/json'})

@app.route('/name')
def print_name():
    return 'Chandrashekhar R'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
