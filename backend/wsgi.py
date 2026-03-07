import sys
import os

# Adiciona a pasta backend/src no path global do Python para que as importações absolutas (src.models...) funcionem
sys.path.insert(0, os.path.dirname(__file__))

# Importa a variável app de src/main.py
from src.main import app

if __name__ == "__main__":
    app.run()
