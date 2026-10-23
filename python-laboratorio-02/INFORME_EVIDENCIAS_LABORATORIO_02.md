# Informe de evidencias - Laboratorio 2

**Aprendiz:** Felipe Andres Navarrete Calderon

**Ficha:** 3388087

**Repositorio:** [laboratorios-tecnica](https://github.com/FelipeNavarrete0313/laboratorios-tecnica)

**Rama de entrega:** `codex/laboratorio-02`
**Estado:** ejercicios verificados; integración del gestor pendiente.

## 1. Trabajo realizado

En este laboratorio practiqué estructuras de control y colecciones en Python. Trabajé condiciones con `if`, `elif` y `else`; ciclos `for` y `while`; listas, tuplas, conjuntos, diccionarios y comprensiones. Para los ejemplos usé datos de productos, categorías, catálogos y ventas.

Los archivos del laboratorio quedaron organizados en la carpeta `python-laboratorio-02`. Entre los ejercicios más representativos están:

| Tema | Archivos relacionados | Qué realicé |
| --- | --- | --- |
| Condiciones | `acceso_sala.py`, `clasificar_nota.py`, `costo_envio.py`, `evaluar_solicitud.py` | Evalué diferentes decisiones según edad, nota, compra, inscripción y documentos. |
| Ciclos | `contador_for*.py`, `contador_while.py`, `hasta_cero.py`, `control_ahorros.py` | Repetí procesos, llevé conteos y acumulé valores hasta una condición de salida. |
| Listas y tuplas | `agregar_elementos.py`, `cambios_inventario.py`, `calificaciones_lista.py`, `categorias_tupla.py` | Agregué, modifiqué, eliminé, recorrí y consulté elementos. |
| Conjuntos y diccionarios | `categorias_distintas.py`, `catalogo_codigo.py`, `catalogo_diccionarios.py`, `buscar_producto_codigo.py` | Eliminé repetidos, busqué por código y representé productos con diccionarios. |
| Comprensiones | `comprension_conjuntos.py`, `comprension_diccionarios.py`, `comprension_lista_diccionarios.py`, `informe_comprensiones.py` | Filtré y resumí datos con estructuras compactas. |

## 2. Estado frente a la guía

La guía propone consolidar un gestor de inventario con menú, registro, actualización, búsqueda y eliminación de productos, además de documentación propia. En el material actual dejé varios ejercicios que sirven como base para ese gestor: búsqueda por código, actualización de precio, catálogo con diccionarios, categorías sin repetir y cálculo de valor del inventario.

Todavía no hay un único archivo `gestor_inventario.py` con menú que integre todas esas opciones, ni módulos `producto.py` e `inventario.py` en esta carpeta. Por eso no lo marco como terminado: es el siguiente paso lógico para convertir los ejercicios aislados en una aplicación única. También queda pendiente agregar un README específico del Laboratorio 2 cuando se haga esa integración.

## 3. Pruebas realizadas

Ejecuté 52 de los 53 archivos del laboratorio con datos de prueba válidos cuando fue necesario. Todos esos 52 terminaron sin errores. Dejé `depuracion_ciclo.py` fuera de las pruebas aprobadas porque su variable `numero` no cambia dentro del `while`; por eso el ciclo se repite sin terminar y sirve como ejercicio de depuración.

| Archivo | Datos usados | Resultado comprobado |
| --- | --- | --- |
| `buscar_producto_codigo.py` | Código `P002` | Mostró `Encontrado: Mouse`. |
| `actualizar_producto.py` | Nuevo precio `90000` | Actualizó el precio de `P001` a `90000.0`. |
| `catalogo_diccionarios.py` | Webcam, 120000, 4 | Agregó el nuevo producto al catálogo. |
| `catalogo_libros.py` | Buscar `L001`; no agregar | Encontró el libro y mantuvo el catálogo. |
| `control_ahorros.py` | -5, 1000, 2000, 0 | Rechazó el depósito negativo y acumuló 3000 en dos depósitos válidos. |
| `calcular-lista_diccionario.py` | Datos incluidos | Calculó un valor de inventario de 545000. |
| `categorias_distintas.py` | Datos incluidos | Mostró categorías únicas usando un conjunto. |

## 4. Seguimiento de commits

| Commit | Cambio | Resultado |
| --- | --- | --- |
| `f5a5d21` - `first commit` | Se creó el README inicial del repositorio. | Se inició el control de versiones. |
| `f4e5722` - `Add files via upload` | Se subió `python-laboratorio-01`. | El primer laboratorio quedó disponible en el repositorio. |
| `d194bcc` - actualización de README | Se ajustó la información del README sobre el Laboratorio 1. | Se actualizó la descripción del repositorio. |
| `f33afc0` - `feat: agregar laboratorio 02` | Se agregó la carpeta `python-laboratorio-02` a esta rama. | Los ejercicios del Laboratorio 2 quedaron versionados sin cachés de Python. |

## 5. Preguntas de análisis situacional

### 1. ¿Qué haría si el gestor no permite registrar dos productos con el mismo código?

Antes de agregar un producto buscaría si el código ya existe en la colección. Si existe, mostraría un mensaje y no usaría `append`, porque el código debe identificar a un solo producto. Lo comprobaría intentando registrar `P001` dos veces: el segundo intento debe rechazarse y la cantidad de productos debe quedar igual.

### 2. ¿Qué haría si el menú vuelve a mostrarse pero se pierden los productos registrados?

Revisaría que la lista o el diccionario principal se cree antes del ciclo `while` del menú, y no dentro de cada opción. De esa forma todas las opciones usan la misma información mientras el programa está abierto. Haría una prueba registrando un producto, regresando al menú y usando la opción de listar; el producto debe seguir apareciendo.

### 3. ¿Qué haría si intentan actualizar las existencias con una cantidad negativa?

Convertiría la entrada a entero y validaría que sea mayor o igual a cero antes de cambiar el producto. Si no cumple, mostraría el error y conservaría la cantidad anterior. Para comprobarlo probaría primero `-2` y verificaría que no cambie nada; después ingresaría una cantidad válida para confirmar que sí se actualiza.

### 4. ¿Qué haría si necesito mostrar categorías sin repetirlas?

Usaría un conjunto, por ejemplo `{producto['categoria'] for producto in productos}`, porque un `set` conserva valores únicos. Es más adecuado que una lista cuando solo necesito categorías diferentes. Lo probaría con varios productos de la misma categoría y revisaría que se muestre una sola vez.

### 5. ¿Qué haría si el resumen del inventario tiene un valor económico incorrecto?

Revisaría que cada producto sume `precio * cantidad`, no solamente uno de esos dos datos. Haría el acumulado con `total += producto['precio'] * producto['cantidad']` y compararía el resultado con una suma manual. También dejaría el caso de prueba anotado para detectar el mismo error después de modificar el programa.
