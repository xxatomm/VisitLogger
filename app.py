from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def log_ip():
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Guardar la información en un archivo de logs
    with open('logs.txt', 'a') as log_file:
        log_file.write(f"IP: {ip_address} - User Agent: {user_agent} - Time: {timestamp}\n")

    return redirect('https://www.microsoft.com/es-pe')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
