class Inventario:
    def __init__(self):
        self._productos = []

    def buscar_por_codigo(self, codigo):
        for prod in self._productos:
            if prod.codigo == codigo:
                return prod
        return None

    def agregar(self, producto):
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def eliminar(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto is not None:
            self._productos.remove(producto)
            return True
        return False

    def listar(self):
        return self._productos.copy()
