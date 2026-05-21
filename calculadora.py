def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def main():
    print("=== Calculadora Simple ===")
    print("Operaciones: suma, resta, multiplicacion, division")

    operacion = input("Elige una operacion: ").strip().lower()
    a = float(input("Primer numero: "))
    b = float(input("Segundo numero: "))

    if operacion == "suma":
        print(f"Resultado: {suma(a, b)}")
    elif operacion == "resta":
        print(f"Resultado: {resta(a, b)}")
    elif operacion == "multiplicacion":
        print(f"Resultado: {multiplicacion(a, b)}")
    elif operacion == "division":
        print(f"Resultado: {division(a, b)}")
    else:
        print("Operacion no reconocida")

if __name__ == "__main__":
    main()
