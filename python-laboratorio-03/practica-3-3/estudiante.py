class Estudiante:
    def __init__(self, nombre, ficha, promedio):
        self.nombre = nombre
        self.ficha = ficha
        self.promedio = promedio

    def mostrar_perfil(self):
        print(f"Estudiante: {self.nombre} | Ficha: {self.ficha} | Promedio: {self.promedio}")

    def aprobo(self):
        return self.promedio >= 3.0

if __name__ == "__main__":
    est1 = Estudiante("Carlos Gómez", 2825001, 2.8)
    est2 = Estudiante("María Rojas", 2825002, 4.1)

    est1.mostrar_perfil()
    print("¿Aprobó Carlos?:", est1.aprobo())

    est2.mostrar_perfil()
    print("¿Aprobó María?:", est2.aprobo())
