# ui_server.py - Flask bridge to your CLI backend
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import subprocess
import json
import os

app = Flask(__name__, static_folder='ui', static_url_path='')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('ui', 'index.html')

@app.route('/api/scan')
def scan_devices():
    try:
        result = subprocess.run(['python', 'discovery_client.py'], 
                              capture_output=True, text=True, timeout=5)
        devices = []
        if result.stdout:
            for line in result.stdout.strip().split('\n'):
                if '|' in line:
                    name, ip = line.split('|', 1)
                    devices.append({'name': name.strip(), 'ip': ip.strip()})
        return jsonify({'devices': devices})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/send', methods=['POST'])
def send_message():
    try:
        data = request.json
        ip = data['ip']
        msg = data['msg']
        subprocess.Popen(['python', 'sender.py', ip, f"MSG:{msg}"], 
                        stdout=subprocess.DEVNULL)
        return jsonify({'status': 'sent'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/start-receiver')
def start_receiver():
    subprocess.Popen(['python', 'receiver.py'], stdout=subprocess.DEVNULL)
    return jsonify({'status': 'receiver_started'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
