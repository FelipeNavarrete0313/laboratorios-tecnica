class Inventario:
    def __init__(self):
        self._productos = []

    def buscar_por_codigo(self, codigo):
        for prod in self._productos:
            if prod.codigo == codigo:
                return prod
        return None

    def registrar_producto(self, producto):
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def listar_productos(self):
        return self._productos.copy()

    def actualizar_existencias(self, codigo, nueva_cantidad):
        prod = self.buscar_por_codigo(codigo)
        if prod is None:
            return False
        return prod.actualizar_existencias(nueva_cantidad)

    def eliminar_producto(self, codigo):
        prod = self.buscar_por_codigo(codigo)
        if prod is not None:
            self._productos.remove(prod)
            return True
        return False

    def productos_sin_stock(self):
        return [prod.nombre for prod in self._productos if prod.cantidad == 0]

    def resumen(self):
        return {
            "total_productos": len(self._productos),
            "unidades_disponibles": sum(p.cantidad for p in self._productos),
            "valor_total": sum(p.calcular_valor() for p in self._productos),
            "categorias_utilizadas": {p.categoria for p in self._productos}
        }
