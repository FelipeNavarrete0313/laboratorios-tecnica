# Informe de evidencias - Laboratorio 3

**Aprendiz:** Felipe Andres Navarrete Calderon

**Ficha:** 3388087

**Repositorio:** [laboratorios-tecnica](https://github.com/FelipeNavarrete0313/laboratorios-tecnica)

**Rama de entrega:** `codex/laboratorio-03`

**Estado:** actividades completadas y verificadas.

## 1. Trabajo realizado

En este laboratorio pasé de ejercicios separados a programas organizados con funciones, módulos y clases. La carpeta contiene 36 archivos Python y un gestor de inventario orientado a objetos en `gestor_inventario`.

El gestor quedó dividido por responsabilidades:

| Archivo | Responsabilidad implementada |
| --- | --- |
| `gestor_inventario/producto.py` | Define la clase `Producto`, valida código, nombre, categoría, precio y cantidad; además calcula el valor del producto y permite actualizar existencias. |
| `gestor_inventario/inventario.py` | Define la clase `Inventario` para registrar, buscar, listar, actualizar, eliminar, identificar productos sin stock y calcular un resumen. |
| `gestor_inventario/main.py` | Presenta el menú e interactúa con el usuario. Las lecturas de precio y cantidad validan el tipo de dato y no aceptan valores inválidos. |
| `gestor_inventario/pruebas_independencia.py` | Comprueba que dos inventarios no comparten accidentalmente la misma lista de productos. |
| `practica3.2/cotizador_modular` | Separa cálculos y validaciones para subtotal, descuento, impuesto y total. |

También trabajé clases y objetos con `Billetera`, `Estudiante` y `CuentaPuntos`; relaciones entre objetos en `relacion_objetos`; módulos de saludo, mensajes, conversiones y validaciones. El README del gestor explica la estructura básica y cómo ejecutarlo desde su carpeta.

## 2. Comparación entre el Laboratorio 2 y el Laboratorio 3

En el Laboratorio 2 los datos se trabajaron principalmente con listas y diccionarios en ejercicios independientes. En este laboratorio agrupé el comportamiento con programación orientada a objetos:

| Aspecto | Laboratorio 2 | Laboratorio 3 |
| --- | --- | --- |
| Producto | Diccionarios y listas en ejercicios individuales. | Instancia de la clase `Producto` con atributos y métodos. |
| Inventario | Operaciones separadas como búsqueda, actualización o cálculo. | Clase `Inventario` que reúne las operaciones sobre una colección propia. |
| Validaciones | Se hacen dentro de cada ejercicio. | Se concentran en el constructor, métodos y funciones de lectura. |
| Interfaz | Entradas puntuales por archivo. | Menú de consola en `main.py` para usar varias operaciones en una misma ejecución. |

## 3. Pruebas realizadas

Probé el menú del gestor, los módulos de cálculo y varios ejercicios de clases. Los resultados principales fueron los siguientes:

| Prueba | Resultado esperado | Resultado observado |
| --- | --- | --- |
| Registrar `P001` - Teclado | El producto debe quedar en el inventario. | Se mostró `Producto registrado exitosamente.` |
| Registrar `P001` por segunda vez | El duplicado debe rechazarse. | Se mostró el mensaje de código existente. |
| Buscar `P001` | Debe recuperar nombre, categoría, precio y cantidad. | Se mostraron los datos de Teclado y 4 unidades. |
| Actualizar `P001` a 0 | Debe aceptar cero y marcarlo sin existencias. | Se actualizó el stock y Teclado apareció en la lista sin existencias. |
| Eliminar `P001` | Debe quitar el producto. | El resumen quedó con 0 productos y valor $0.0. |
| Prueba de independencia | Un inventario no debe modificar otro. | Imprimió `Primero: 1` y `Segundo: 0`. |
| Cotizador modular | 200000 - 20000 + 34200 = 214200. | Mostró `Total: 214200`. |
| `leer_cantidad.py` | Debe rechazar texto y negativos antes de aceptar un entero. | Rechazó `abc` y `-2`; aceptó `5`. |

## 4. Estado, dificultades y mejoras

Las operaciones principales del gestor funcionan en las pruebas: registrar, buscar, actualizar, eliminar, listar productos sin stock y mostrar resumen. No tuve una dificultad que impidiera ejecutar el programa.

Como mejoras futuras, puedo agregar pruebas automatizadas, una mejor presentación de las listas y persistencia en archivos. Esa última mejora se trabaja en el Laboratorio 4.

## 5. Seguimiento de commits

| Commit | Cambio | Resultado |
| --- | --- | --- |
| `f5a5d21` - `first commit` | Se creó el README inicial. | Se inició el repositorio. |
| `f4e5722` - `Add files via upload` | Se subió el Laboratorio 1. | El primer laboratorio quedó disponible. |
| `d194bcc` - actualización de README | Se actualizó la información del Laboratorio 1. | Se mejoró la descripción del repositorio. |
| `3eefb54` - `Subida del laboratorio 3` | Se agregó la carpeta completa de este laboratorio a esta rama. | El código de funciones, módulos y POO quedó versionado. |

## 6. Preguntas de análisis situacional

### 1. ¿Qué haría si alguien intenta cambiar directamente el precio o la cantidad de un producto por un valor negativo?

Mantendría los datos protegidos dentro de `Producto` y permitiría los cambios solo por métodos o propiedades con validación. El código actual controla que el precio sea mayor que cero y que la cantidad no sea negativa al crear el producto; `actualizar_existencias` también rechaza negativos. Si necesitara modificar el precio después de crearlo, agregaría un setter con la misma regla. Lo comprobaría intentando enviar `-1` y verificando que el valor anterior no cambie.

### 2. ¿Qué revisaría si agrego un producto a un inventario y también aparece en otro?

Revisaría que la lista de productos se cree dentro de `__init__` de cada instancia, y no como atributo compartido de la clase. También comprobaría que cada inventario reciba su propio objeto o colección. Ya hice una prueba: agregué un producto al primer inventario y el segundo quedó con cero productos. Si eso deja de suceder, revisaría dónde se está compartiendo la lista.

### 3. ¿Qué haría si necesito mostrar información de un producto, pero la clase no debe usar `input()` ni controlar el menú?

Mantendría la clase `Producto` enfocada en sus atributos y métodos. Desde `main.py` buscaría el objeto, leería sus propiedades y formatearía el mensaje. Así se separa la lógica de negocio de la interfaz de consola. Lo comprobaría buscando un código existente y verificando que los datos se muestren sin que la clase dependa de `input()`.

### 4. ¿Cómo usaría un método que calcula el valor de un producto pero no imprime el resultado?

Usaría `calcular_valor()` para recibir `precio * cantidad` y guardaría ese retorno en una variable. Después `Inventario` puede sumarlo en el resumen y `main.py` decide cómo mostrarlo. Esto permite reutilizar el cálculo sin copiar la fórmula. Lo probaría con precio 85000 y cantidad 4: el método debe devolver 340000 antes de imprimir cualquier texto.

### 5. ¿Qué haría si el proyecto deja de ejecutarse después de cambiar módulos?

Leeré el error de importación o de sintaxis y revisaré desde qué carpeta estoy ejecutando `main.py`. Confirmaría que los nombres de los módulos coincidan con los `import` y ejecutaría primero el módulo afectado; después probaría el menú completo. Si el cambio ya está versionado, compararía con `git diff` el último commit funcional y dejaría un commit descriptivo cuando corrija el problema.
