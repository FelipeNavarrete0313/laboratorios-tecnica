# Gestor de Inventario Persistente (Laboratorio 4)

Aplicación de consola orientada a objetos con persistencia en JSON, exportación tabular a CSV y arquitectura desacoplada.

## Ejecución

Para iniciar el gestor, asegúrate de estar en el directorio `gestor_inventario`:

```bash
python main.py
```

## Arquitectura de Módulos

- `producto.py`: Encapsula atributos y reglas de negocio mediante `@property`. Incluye serialización (`a_diccionario`) y deserialización (`desde_diccionario`).
- `inventario.py`: Administra la colección interna en memoria de objetos `Producto`. Mantiene aislamiento frente a operaciones de E/S.
- `almacenamiento.py`: Maneja lectura y escritura robusta en `datos/productos.json` utilizando `pathlib`.
- `reportes.py`: Genera `reportes/inventario.csv` calculando columnas analíticas como `valor_inventario`.
- `main.py`: Interfaz de usuario por consola, lectura controlada y captura de excepciones.
