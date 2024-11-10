# VisitLogger

## 📋 Descripción
VisitLogger es una aplicación en Python que utiliza Flask para registrar información de los visitantes, incluyendo su dirección IP, User-Agent, referer, idioma preferido, y más. Además, redirige automáticamente a los usuarios a una URL específica después de registrar la información.

## 🚀 Características
- Registro de dirección IP, navegador, referer, idioma y más.
- Redirección automática a una página web.
- Guarda la información en un archivo `logs.txt` para auditoría.

## 📂 Estructura del Proyecto

```bash
VisitLogger/
├── app.py
├── requirements.txt
├── README.md
├── cert.pem (solo si usas HTTPS)
├── key.pem (solo si usas HTTPS)
├── logs.txt (archivo generado para registros)
└── venv/ (directorio del entorno virtual)
```

## 🛠️ Requisitos Previos
Antes de ejecutar la aplicación, asegúrate de tener instalados los siguientes programas:

Python 3
pip (gestor de paquetes de Python)
Flask

## ⚙️ Instalación y Configuración
Sigue estos pasos para clonar y ejecutar el proyecto:

1. Clona el repositor
```bash
git clone https://github.com/xxatomm/VisitLogger.git
cd VisitLogger
```

2. Crea un entorno virtual y actívalo
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instala las dependencias
```bash
pip install -r requirements.txt
```

4. (Opcional) Generar certificados SSL para HTTPS
Si deseas utilizar HTTPS, ejecuta este comando:
```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

5. Ejecuta la aplicación
Para ejecutar la aplicación en modo HTTP:
```bash
python3 app.py
```

Si estás usando HTTPS, usa el siguiente comando:
```bash
python3 app.py --https
```

6. Accede a la aplicación en tu navegador
- HTTP: http://localhost:5000 o http://<tu-ip>:5000 desde otro dispositivo en la red.
- HTTPS: https://localhost:5000 o https://<tu-ip>:5000.

## 📜 Uso y Registro de Información
Cada vez que un usuario accede a la aplicación, se registra la siguiente información en el archivo logs.txt:

- Dirección IP del visitante
- User-Agent (navegador y dispositivo)
- Referer (página de origen)
- Idioma preferido del navegador
- Método de solicitud (GET, POST, etc.)
- Fecha y hora del acceso

## 📄 Ejemplo de Registro en logs.txt
```bash
--- NUEVO REGISTRO ---
Fecha y Hora: 2024-11-09 21:00:13
IP del Visitante: 192.168.18.79
User Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Referer: https://google.com
Idioma Preferido: es-ES,es;q=0.9
Método de Solicitud: GET
Encabezados: {'Host': 'localhost:5000', 'Connection': 'keep-alive', ...}
-----------------------
```

## 🔧 Resolución de Problemas
Si ves un error similar a Bad request version, asegúrate de:

- Usar http:// en lugar de https:// si no has configurado HTTPS.
- Ejecutar la aplicación en un puerto diferente si el puerto 5000 está en uso
