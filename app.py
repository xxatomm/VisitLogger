from flask import Flask, redirect, request
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/')
def log_visitor():
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    referrer = request.referrer if request.referrer else "Sin referer"
    language = request.headers.get('Accept-Language', 'No especificado')
    method = request.method
    headers = dict(request.headers)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    server_ip = socket.gethostbyname(socket.gethostname())
    server_host = socket.gethostname()

    log_entry = f"""
--- NUEVO REGISTRO ---
Fecha y Hora: {timestamp}
IP del Visitante: {ip_address}
User Agent: {user_agent}
Referer: {referrer}
Idioma Preferido: {language}
Método de Solicitud: {method}
Encabezados:
{headers}
IP del Servidor: {server_ip}
Nombre del Host del Servidor: {server_host}
-----------------------
"""
    with open('logs.txt', 'a') as log_file:
        log_file.write(log_entry)

    return redirect('https://www.microsoft.com/es-pe', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
