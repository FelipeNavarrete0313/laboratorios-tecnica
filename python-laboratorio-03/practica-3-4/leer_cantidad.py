def pedir_cantidad():
    while True:
        entrada = input("Cantidad: ").strip()
        try:
            cantidad = int(entrada)
        except ValueError:
            print("Debes escribir un entero.\n")
            continue

        if cantidad < 0:
            print("La cantidad no puede ser negativa.\n")
            continue

        print(f"Cantidad aceptada: {cantidad}")
        return cantidad

if __name__ == "__main__":
    pedir_cantidad()
