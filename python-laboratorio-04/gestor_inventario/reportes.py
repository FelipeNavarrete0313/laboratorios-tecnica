import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CARPETA_REPORTES = BASE_DIR / "reportes"
RUTA_CSV = CARPETA_REPORTES / "inventario.csv"


def exportar_csv(inventario):
    CARPETA_REPORTES.mkdir(parents=True, exist_ok=True)
    productos = inventario.listar_todos()

    filas = []
    for p in productos:
        filas.append({
            "codigo": p.codigo,
            "nombre": p.nombre,
            "categoria": p.categoria,
            "precio": p.precio,
            "cantidad": p.cantidad,
            "valor_inventario": p.precio * p.cantidad
        })

    campos = ["codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario"]

    with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas)

    return RUTA_CSV
