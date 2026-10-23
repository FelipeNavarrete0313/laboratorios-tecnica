nombre = input("Ingrese su nombre: ")
producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))
porcentaje_descuento = int(input("Ingrese el porcentaje de descuento: "))
porcentaje_impuesto = int(input("Ingrese el porcentaje de impuesto: "))
costo_envio = float(1000)
nombre_vendedror = input("Ingrese el nombre del vendedor: ")
codigo_cotizacion = input("Ingrese el código de cotización: ")


subtotal = precio_unitario * cantidad


valor_descuento = subtotal * (porcentaje_descuento / 100)
base_descuento = subtotal - valor_descuento
valor_impuesto = base_descuento * (porcentaje_impuesto / 100)
total = base_descuento + valor_impuesto+ costo_envio
print("Subtotal: $", subtotal)
print("Costo de envío: $", costo_envio)
print("Nombre del vendedor:", nombre_vendedror)
print("Código de cotización:", codigo_cotizacion)

print("Total: $", total)