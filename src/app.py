from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify(
        {
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'host': socket.gethostname() 
        }
    )

@app.route('/api/v1/health')
def health():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")