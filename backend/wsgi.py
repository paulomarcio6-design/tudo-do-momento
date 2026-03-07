import sys
import os

# Define o caminho absoluto da pasta `backend` e adiciona ao sys.path
# Isso garante que imports como `from src.models...` funcionem independente de onde o gunicorn for rodado
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Agora podemos importar do src.main sem problemas
from src.main import app

if __name__ == "__main__":
    app.run()
