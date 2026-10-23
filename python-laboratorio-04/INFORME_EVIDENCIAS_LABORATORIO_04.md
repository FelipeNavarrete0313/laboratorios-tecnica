# Informe de evidencias - Laboratorio 4

**Aprendiz:** Felipe Andres Navarrete Calderon

**Ficha:** 3388087

**Repositorio:** [laboratorios-tecnica](https://github.com/FelipeNavarrete0313/laboratorios-tecnica)

**Rama de entrega:** `codex/laboratorio-04`

**Estado:** actividades completadas y verificadas.

## 1. Trabajo realizado

En este laboratorio amplié el gestor de inventario para conservar la información fuera de la memoria del programa. Trabajé manejo de excepciones, lectura y escritura de archivos, JSON, CSV, rutas con `pathlib`, validaciones, serialización, herencia, composición y polimorfismo.

El gestor de inventario quedó organizado por módulos:

| Archivo | Responsabilidad implementada |
| --- | --- |
| `gestor_inventario/producto.py` | Protege los datos de cada producto con propiedades; valida código, nombre, categoría, precio numérico finito y positivo, y cantidad entera no negativa. También serializa y reconstruye objetos. |
| `gestor_inventario/inventario.py` | Gestiona la colección de productos, evita códigos repetidos, calcula el resumen y carga datos en una instancia temporal para no dejar el inventario a medias si un registro falla. |
| `gestor_inventario/almacenamiento.py` | Guarda y carga `datos/productos.json` usando una ruta calculada desde `__file__`. Captura errores de JSON y validación durante la carga. |
| `gestor_inventario/reportes.py` | Genera `reportes/inventario.csv` con las columnas de cada producto y el campo calculado `valor_inventario`. |
| `gestor_inventario/main.py` | Controla el menú, lectura segura de enteros y flotantes, guardado automático, exportación a CSV y modo de solo lectura ante un archivo dañado. |

Además, desarrollé las prácticas de manejo de errores (`practica-4-1`), archivos de texto (`practica-4-2`), JSON y CSV (`practica-4-3`) y conceptos de POO como herencia, sobrescritura y polimorfismo (`practica-4-4`). El archivo `RESPUESTAS_COMPROBACION_Y_ANALISIS.md` documenta las comprobaciones de esas prácticas.

## 2. Comparación entre el Laboratorio 3 y el Laboratorio 4

El Laboratorio 3 tiene un gestor en memoria basado en clases. En este laboratorio conservé esa organización y agregué persistencia y reportes:

| Aspecto | Laboratorio 3 | Laboratorio 4 |
| --- | --- | --- |
| Datos | Se mantienen mientras el programa está abierto. | Se guardan en `productos.json` y se recuperan al iniciar. |
| Validaciones | Valida datos al crear o actualizar productos. | Refuerza las validaciones con propiedades, tipos, precios finitos y manejo de errores de carga. |
| Reportes | Muestra resumen en consola. | Exporta un CSV con el valor de inventario por producto. |
| Organización | `Producto`, `Inventario` y `main.py`. | Añade `almacenamiento.py` y `reportes.py` para separar persistencia y exportación. |

## 3. Pruebas realizadas

Probé el gestor con información controlada y revisé los archivos generados durante la ejecución. Las pruebas se realizaron en una copia local de trabajo para no incluir los archivos temporales de prueba dentro de la entrega.

| Prueba | Resultado observado |
| --- | --- |
| Registrar producto | Registré `P010`, Webcam, Periféricos, precio 120000 y cantidad 5. El programa confirmó el registro y guardó el inventario. |
| Exportar CSV | Se creó `inventario.csv` con `valor_inventario` igual a 600000.0, que corresponde a 120000 x 5. |
| Actualizar existencias | Cambié la cantidad de `P010` a 0. El programa guardó de nuevo y la consulta sin stock mostró `[P010] Webcam`. |
| Recuperar información | Al ejecutar otra vez el programa, recuperó `P010` desde JSON con precio 120000.00 y stock 0. |
| División segura | Con dividendo 10 y divisor 0, informó que no es posible dividir entre cero sin mostrar una excepción sin controlar. |
| Conversión segura | Con la entrada `abc`, informó que se debe ingresar un número entero y terminó el programa normalmente. |
| Producto validado | Al usar precio -5000, rechazó la creación con el mensaje de precio positivo. |

## 4. Estado, dificultades y mejoras

Las pruebas confirmaron que el gestor registra, guarda, recupera, actualiza, exporta y calcula datos del inventario. No tuve una dificultad que bloqueara la ejecución.

Como siguiente mejora, puedo añadir pruebas automatizadas para la carga de JSON dañado y para el reporte CSV. También puedo ampliar el formato del reporte con fecha de generación o totales generales si la guía lo solicita.

## 5. Seguimiento de commits

| Commit | Cambio | Resultado |
| --- | --- | --- |
| `f5a5d21` - `first commit` | Se creó el README inicial. | Se inició el repositorio. |
| `f4e5722` - `Add files via upload` | Se subió el Laboratorio 1. | El primer laboratorio quedó disponible. |
| `d194bcc` - actualización de README | Se actualizó la información del Laboratorio 1. | Se mejoró la descripción principal. |
| `ee2a9a8` - `Subida del laboratorio 4` | Se agregó la carpeta `python-laboratorio-04` a esta rama. | Quedaron versionados el gestor, las prácticas y la documentación existente. |

## 6. Preguntas de análisis situacional

### 1. ¿Qué haría si cierro el programa y al volver no aparece el inventario?

Primero revisaría si `productos.json` existe, si la ruta es la esperada y qué contenido tiene. Confirmaría que el guardado se llame después de registrar, actualizar o eliminar, y que la carga use la misma ruta creada desde `__file__`. Para comprobarlo, registraría un producto, cerraría la aplicación y la abriría de nuevo; el producto debe aparecer en la lista y coincidir con el contenido del JSON.

### 2. ¿Qué haría si `productos.json` existe, pero tiene un error de sintaxis?

No lo trataría como un inventario vacío ni lo sobrescribiría. Capturaría `json.JSONDecodeError`, mostraría una alerta y bloquearía las operaciones que puedan guardar encima del archivo, como hace el modo de solo lectura en `main.py`. Lo probaría eliminando una coma en una copia del JSON y verificando que el programa avise sin modificar el archivo dañado. Después corregiría el JSON y volvería a probar la carga.

### 3. ¿Qué haría si al cargar un JSON aparecen productos con códigos repetidos o cantidades negativas?

Dejaría que `Producto` e `Inventario` validen los datos durante la carga en un inventario temporal. Si uno falla, no reemplazaría el inventario activo por datos incompletos. Para comprobarlo, usaría un JSON con dos productos `P001` o una cantidad negativa; la carga debe detenerse e informar el problema sin dejar la colección parcialmente cargada.

### 4. ¿Qué haría si el CSV muestra solo el precio y no el valor del inventario?

Revisaría `reportes.py`, porque allí se crea cada fila. El valor correcto es `precio * cantidad`, no solo `precio`. Con una Webcam de 120000 y cantidad 5, el CSV debe mostrar 600000.0 en `valor_inventario`. Abriría el CSV exportado y compararía esa celda con la multiplicación manual.

### 5. ¿Cómo investigaría una regresión después de modificar el almacenamiento?

Usaría `git log` para ubicar el último commit que cargaba correctamente y `git diff` para comparar el formato que se guarda con lo que `desde_diccionario()` espera. Revisaría las claves `codigo`, `nombre`, `categoria`, `precio` y `cantidad`. Después probaría todo el flujo: registrar, guardar, cerrar, abrir y listar. Cuando localice la causa, dejaría un commit que describa el ajuste aplicado y la prueba con la que lo comprobé.
