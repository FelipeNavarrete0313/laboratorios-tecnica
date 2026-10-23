import calculos
import validaciones

def ejecutar():
    precio = 100000.0
    cantidad = 2
    descuento = 10.0
    impuesto = 19.0

    if not (validaciones.precio_valido(precio) and
            validaciones.cantidad_valida(cantidad) and
            validaciones.porcentaje_valido(descuento) and
            validaciones.porcentaje_valido(impuesto)):
        print("Datos no válidos.")
        return

    subtotal = calculos.calcular_subtotal(precio, cantidad)
    monto_descuento = calculos.calcular_descuento(subtotal, descuento)
    base = subtotal - monto_descuento
    monto_impuesto = calculos.calcular_impuesto(base, impuesto)
    total = base + monto_impuesto

    print(f"Subtotal: {int(subtotal)}")
    print(f"Descuento: {int(monto_descuento)}")
    print(f"Base después del descuento: {int(base)}")
    print(f"Impuesto: {int(monto_impuesto)}")
    print(f"Total: {int(total)}")

if __name__ == "__main__":
    ejecutar()
