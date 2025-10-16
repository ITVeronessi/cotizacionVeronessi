#!/bin/bash
echo "🚀 Iniciando servidor FastAPI..."

# Moverse a la raíz del proyecto (la carpeta que contiene "backend")
cd "$(dirname "$0")/.." || exit

# Confirmar ruta
echo "📂 Directorio actual: $(pwd)"

APP_PATH="backend.main:app"
HOST="127.0.0.1"
PORT="8000"

python -m uvicorn $APP_PATH --host $HOST --port $PORT --reload