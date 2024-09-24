def es_perfecto(n):
    suma_divisores = sum([i for i in range(1, n) if n % i == 0])
    return suma_divisores == n

for i in range(1, 1000):
    if es_perfecto(i):
        print(f"Número perfecto: {i}")
