numeros = []
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").lower()
    if respuesta == "no":
        break
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {len(pares)}")
print(f"Cantidad de números impares: {len(impares)}")