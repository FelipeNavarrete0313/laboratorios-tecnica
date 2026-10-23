# Gestor de Inventario - POO

## Descripción
Aplicación de consola para la administración de inventarios desarrollada bajo el paradigma orientado a objetos (POO), con modularidad, propiedades encapsuladas y validación de tipos y dominios de datos.

## Estructura del proyecto
- `producto.py`: Entidad individual `Producto` con control estricto de atributos, métodos y validaciones con `ValueError`.
- `inventario.py`: Contenedor `Inventario` para manejar colecciones independientes de instancias `Producto`.
- `main.py`: Punto de entrada interactivo por consola con captura de excepciones.
- `pruebas_independencia.py`: Script de verificación para evitar estados mutables compartidos entre instancias.

## Ejecución
```bash
python main.py
```
