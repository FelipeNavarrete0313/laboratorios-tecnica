from producto import Producto
from inventario import Inventario

inv = Inventario()

print("Registro P001:", inv.agregar(Producto("P001", "Teclado")))
print("Registro P002:", inv.agregar(Producto("P002", "Mouse")))
print("Registro P001 repetido:", inv.agregar(Producto("P001", "Otro Teclado")))
print("Eliminar P999:", inv.eliminar("P999"))
print("Eliminar P001:", inv.eliminar("P001"))
