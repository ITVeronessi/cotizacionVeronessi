#!/bin/bash
#!/bin/bash
echo "🚀 Iniciando servidor FastAPI..."

# Moverse a la raíz del proyecto (la carpeta que contiene "backend")
cd "$(dirname "$0")/.." || exit
echo "📂 Directorio actual: $(pwd)"

# Host y puerto
HOST="0.0.0.0"
PORT=${PORT:-8000}  # Render asigna PORT automáticamente

# Activar virtual environment si existe
if [ -f "./venv/bin/activate" ]; then
    echo "🟢 Activando venv..."
    source ./venv/bin/activate
fi

APP_PATH="backend.main:app"

# Ejecutar Uvicorn
python -m uvicorn $APP_PATH --host $HOST --port $PORT --reload
