import math
from almacenamiento import cargar_inventario, guardar_inventario
from producto import CATEGORIAS, Producto
from reportes import exportar_csv


def leer_entero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")


def leer_flotante(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
            if not math.isfinite(valor):
                print("Entrada inválida. Ingrese un número finito.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Debe ser un número.")


def mostrar_menu():
    print("\n================================")
    print("       GESTOR DE INVENTARIO     ")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("8. Guardar inventario")
    print("9. Exportar reporte CSV")
    print("0. Salir")


def main():
    inventario, error = cargar_inventario()

    modo_solo_lectura = False
    if error is not None:
        print(f"\n[ERROR DE CARGA] Archivo dañado o inconsistente: {error}")
        print("Para proteger la integridad de los datos, el guardado automático está bloqueado.")
        modo_solo_lectura = True
        from inventario import Inventario
        inventario = Inventario()
    else:
        print("\nInventario inicializado correctamente.")

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            if modo_solo_lectura:
                print("Operación bloqueada por persistencia protegida.")
                continue
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            print(f"Categorías permitidas: {', '.join(CATEGORIAS)}")
            categoria = input("Categoría: ").strip()
            precio = leer_flotante("Precio: ")
            cantidad = leer_entero("Cantidad: ")

            try:
                prod = Producto(codigo, nombre, categoria, precio, cantidad)
                inventario.agregar_producto(prod)
                print("Producto registrado exitosamente.")
                try:
                    guardar_inventario(inventario)
                    print("Inventario guardado.")
                except Exception as e:
                    print(f"Advertencia: No se pudo guardar en disco ({e}).")
            except (ValueError, TypeError) as err:
                print(f"Error al registrar: {err}")

        elif opcion == "2":
            prods = inventario.listar_todos()
            if not prods:
                print("El inventario está vacío.")
            else:
                print("\n--- Lista de Productos ---")
                for p in prods:
                    print(p)

        elif opcion == "3":
            codigo = input("Código a buscar: ")
            p = inventario.buscar_por_codigo(codigo)
            if p:
                print("\nProducto encontrado:\n", p)
            else:
                print(f"No existe ningún producto con el código '{codigo}'.")

        elif opcion == "4":
            if modo_solo_lectura:
                print("Operación bloqueada por persistencia protegida.")
                continue
            codigo = input("Código: ")
            nueva_cantidad = leer_entero("Nueva cantidad: ")
            try:
                if inventario.actualizar_existencias(codigo, nueva_cantidad):
                    print("Existencias actualizadas.")
                    guardar_inventario(inventario)
                    print("Inventario guardado.")
                else:
                    print("Producto no encontrado.")
            except (ValueError, TypeError) as err:
                print(f"Error en validación: {err}")

        elif opcion == "5":
            if modo_solo_lectura:
                print("Operación bloqueada por persistencia protegida.")
                continue
            codigo = input("Código a eliminar: ")
            if inventario.eliminar_producto(codigo):
                print("Producto eliminado.")
                guardar_inventario(inventario)
                print("Inventario guardado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "6":
            sin_stock = inventario.obtener_sin_stock()
            if not sin_stock:
                print("Todos los productos tienen existencias disponibles.")
            else:
                print("\n--- Productos sin Stock ---")
                for p in sin_stock:
                    print(f"[{p.codigo}] {p.nombre}")

        elif opcion == "7":
            res = inventario.obtener_resumen()
            print("\n--- Resumen del Inventario ---")
            print(f"Productos registrados: {res['total_productos']}")
            print(f"Unidades disponibles: {res['total_unidades']}")
            print(f"Valor total: ${res['valor_total']:.1f}")
            print(f"Categorías utilizadas: {res['categorias_usadas']}")

        elif opcion == "8":
            if modo_solo_lectura:
                print("Guardado cancelado: No se sobrescribirá un archivo en estado dañado.")
                continue
            try:
                ruta = guardar_inventario(inventario)
                print(f"Inventario persistido en: {ruta}")
            except Exception as e:
                print(f"Error al escribir archivo: {e}")

        elif opcion == "9":
            try:
                ruta = exportar_csv(inventario)
                print(f"Reporte exportado: {ruta}")
            except Exception as e:
                print(f"Error exportando CSV: {e}")

        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
