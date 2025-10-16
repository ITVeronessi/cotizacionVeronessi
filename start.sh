#!/bin/bash
echo "🚀 Iniciando servidor FastAPI..."

# Confirmar ruta
echo "📂 Directorio actual: $(pwd)"

APP_PATH="main:app"       # Ahora main.py está en la raíz
HOST="0.0.0.0"
PORT=${PORT:-8000}        # Render asigna el puerto automáticamente

python -m uvicorn $APP_PATH --host $HOST --port $PORT --reload
