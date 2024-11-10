from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def log_visitor():
    # Obtener información del visitante
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    referrer = request.referrer if request.referrer else "No referer"
    language = request.headers.get('Accept-Language')
    method = request.method
    headers = dict(request.headers)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Guardar la información en un archivo de logs
    with open('logs.txt', 'a') as log_file:
        log_file.write(f"""
--- NUEVO REGISTRO ---
IP: {ip_address}
User Agent: {user_agent}
Referer: {referrer}
Idioma: {language}
Método de Solicitud: {method}
Hora: {timestamp}
Encabezados: {headers}
-----------------------
""")

    return redirect('https://www.microsoft.com/es-pe')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
