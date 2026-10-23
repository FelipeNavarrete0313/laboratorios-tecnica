import math

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("El código no puede estar vacío.")
        self._codigo = valor.strip().upper()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if valor not in CATEGORIAS:
            raise ValueError(f"Categoría inválida. Permitidas: {', '.join(CATEGORIAS)}")
        self._categoria = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("El precio debe ser un número.")
        if not math.isfinite(valor):
            raise ValueError("El precio debe ser un número finito.")
        if valor <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        self._precio = float(valor)

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if not isinstance(valor, int):
            raise TypeError("La cantidad debe ser un número entero.")
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = valor

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"]
        )

    def __str__(self):
        return (f"[{self.codigo}] {self.nombre} | Cat: {self.categoria} | "
                f"Precio: ${self.precio:.2f} | Stock: {self.cantidad}")
