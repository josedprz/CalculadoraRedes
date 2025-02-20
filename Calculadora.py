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
                continue
            case 2:
                # Resta
                continue
            case 3:
                # Multiplicación
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                resultado = num1 * num2
                print(f"El resultado de {num1} * {num2} es: {resultado}")
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