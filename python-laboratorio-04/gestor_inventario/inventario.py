from producto import Producto


class Inventario:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar instancias de Producto.")
        if self.buscar_por_codigo(producto.codigo) is not None:
            raise ValueError(f"Ya existe un producto con el código '{producto.codigo}'.")
        self._productos.append(producto)

    def buscar_por_codigo(self, codigo):
        codigo_buscado = codigo.strip().upper()
        for prod in self._productos:
            if prod.codigo == codigo_buscado:
                return prod
        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        producto.cantidad = nueva_cantidad
        return True

    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def listar_todos(self):
        return list(self._productos)

    def obtener_sin_stock(self):
        return [p for p in self._productos if p.cantidad == 0]

    def obtener_resumen(self):
        total_productos = len(self._productos)
        total_unidades = sum(p.cantidad for p in self._productos)
        valor_total = sum(p.precio * p.cantidad for p in self._productos)
        categorias_usadas = len(set(p.categoria for p in self._productos))
        return {
            "total_productos": total_productos,
            "total_unidades": total_unidades,
            "valor_total": valor_total,
            "categorias_usadas": categorias_usadas
        }

    def exportar_datos(self):
        return [p.a_diccionario() for p in self._productos]

    def cargar_desde_lista_diccionarios(self, lista_datos):
        inventario_temporal = Inventario()
        for d in lista_datos:
            prod = Producto.desde_diccionario(d)
            inventario_temporal.agregar_producto(prod)
        self._productos = inventario_temporal._productos
