def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

suma_primos = sum([i for i in range(100) if es_primo(i)])
print(f"La suma de todos los números primos menores que 100 es: {suma_primos}")