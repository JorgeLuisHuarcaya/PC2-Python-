def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número entero no negativo: "))
print(f"El factorial de {numero} es {factorial(numero)}")