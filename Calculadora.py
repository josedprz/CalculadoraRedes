# Funciones

def potencia(num, exponente):
    return num ** exponente

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
                continue
            case 4:
                # División
                continue
            case 5:
                # Potencia
                print('\n-> Potencia <-\n')
                resultado = potencia(int(input("Ingresa el número: ")), int(input("Ingresa el exponente: ")))
                print(f" \n----- El resultado es: {resultado} -----\n")
            case 6:
                break
            case _:
                print("Opcion no válida")

if __name__ == "__main__":
    calculadora()