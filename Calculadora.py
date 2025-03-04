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
                print("Ingresa los números a sumar: ")
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                print("Resultado:", num1 + num2)
                continue
            case 2:
                # Resta
                print("Ingresa los números a restar: ")
                num1 = float(input("Número 1: ")) 
                num2 = float(input("Número 2: "))
                print("Resultado: ", num1 - num2)
            case 3:
                # Multiplicación
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                resultado = num1 * num2
                print(f"El resultado de {num1} * {num2} es: {resultado}")
            case 4:
                # Division
                print("Ingresa los números a dividir: ")
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                print("Resultado división:", num1 / num2)
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