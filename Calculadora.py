# Funciones

def calculadora():
    while True:
        print("Selecciona una operación: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Salir")
        opcion = int(input("Elige una opción: "))
        match opcion:
            case 1:
                # Suma
                print("Ingresa los números a sumar: ")
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                print("Resultado:", num1 + num2)
                continue
            case 2:
                # Resta
                continue
            case 3:
                # Multiplicación
                continue
            case 4:
                # División
                continue
            case 5:
                # Potencia
                continue
            case 6:
                break
            case _:
                print("Opcion no válida")

if __name__ == "__main__":
    calculadora()