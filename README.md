# VisitLogger 📝

## 📋 Descripción
**VisitLogger** es una aplicación web construida con **Flask** en **Python** que permite registrar información de los visitantes a tu servidor. Cada vez que un usuario accede, se registra su **dirección IP**, **User-Agent**, **referer**, **idioma preferido**, y más. Además, la aplicación redirige automáticamente a los usuarios a una URL específica después de registrar la información.

## 🚀 Características
- 🌍 **Registro de información del visitante**: Dirección IP, User-Agent, referer, idioma, y más.
- 🔗 **Redirección automática** a una página web (por ejemplo, Microsoft).
- 📑 **Generación de un archivo de registros** (`logs.txt`) para auditoría y seguimiento.
- 📊 **Fácil de exponer a Internet** usando herramientas como **Serveo** o **ngrok**.

## 📂 Estructura del Proyecto

```bash
VisitLogger/
├── app.py               # Código principal de la aplicación
├── requirements.txt     # Dependencias necesarias
├── README.md            # Este archivo
├── logs.txt             # Archivo generado con los registros
└── venv/                # Directorio del entorno virtual (si se usa)
```

## 🛠️ Requisitos Previos
Antes de ejecutar la aplicación, asegúrate de tener instalados los siguientes programas:

- Python 3 🐍
- pip (gestor de paquetes de Python) 📦
- Flask 🌐

## ⚙️ Instalación y Configuración
Sigue estos pasos para clonar y ejecutar el proyecto:

1. Clona el repositorio
Primero, clona el repositorio a tu máquina local:
```bash
git clone https://github.com/xxatomm/VisitLogger.git
cd VisitLogger
```

2. Crea un entorno virtual y actívalo (opcional pero recomendado)
Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instala las dependencias
Una vez dentro del entorno virtual, instala las dependencias del proyecto usando pip:
```bash
pip install -r requirements.txt
```
4. (Opcional) Exponer la aplicación usando Serveo
Si deseas exponer tu servidor Flask a Internet sin pagar por servicios como ngrok, puedes usar Serveo:

- Abre una terminal y navega a la carpeta donde tienes el proyecto.
- Ejecuta el siguiente comando para crear un túnel SSH con Serveo y exponer tu servidor local:

```bash
ssh -R 80:localhost:5000 serveo.net
```
Esto generará una URL pública que puedes compartir con otros.

5. Ejecuta la aplicación
Para ejecutar la aplicación localmente:
```bash
python3 app.py
```
La aplicación estará disponible en http://127.0.0.1:5000/ por defecto. Si usas Serveo, puedes compartir la URL generada.

## 📜 Uso y Registro de Información

Cada vez que un usuario accede a la aplicación, se registra la siguiente información en el archivo logs.txt:
- 🌍 Dirección IP del visitante.
- 🕵️‍♂️ User-Agent (información sobre el navegador y el dispositivo).
- 🔗 Referer (página de origen).
- 🌐 Idioma preferido del navegador.
- 📝 Método de solicitud (GET, POST, etc.).
- 📅 Fecha y hora del acceso.

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
Si ves un error como "Bad request version", asegúrate de lo siguiente:

- Usa http:// en lugar de https:// si no has configurado HTTPS.
- Ejecuta la aplicación en un puerto diferente si el puerto 5000 ya está en uso.
