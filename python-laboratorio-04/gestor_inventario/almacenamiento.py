import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"


def guardar_inventario(inventario):
    RUTA_JSON.parent.mkdir(parents=True, exist_ok=True)
    datos = inventario.exportar_datos()
    with RUTA_JSON.open("w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
    return RUTA_JSON


def cargar_inventario():
    from inventario import Inventario
    inventario = Inventario()

    if not RUTA_JSON.exists():
        return inventario, None

    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        inventario.cargar_desde_lista_diccionarios(datos)
        return inventario, None
    except (json.JSONDecodeError, ValueError, TypeError, KeyError) as error:
        return None, str(error)
