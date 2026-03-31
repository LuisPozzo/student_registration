# storage.py

import json
from data import students
from pathlib import Path

# Obtener la ruta absoluta del archivo actual (storage.py)
ruta = Path(__file__).resolve().parent
file_path =ruta / "students.json"


def save_data():
    """
    Guarda los datos en un archivo JSON en la misma carpeta.
    """
    with open(file_path, "w") as file:
        json.dump(students, file, indent=4)

def load_data():
    """
    Carga los datos desde un archivo JSON si existe.
    """
    try:
        if file_path.exists():
            with open("students.json", "r") as file:
                data = json.load(file)
                students.clear()
                students.extend(data)
    except FileNotFoundError:
        # Si no existe el archivo, no pasa nada
        pass