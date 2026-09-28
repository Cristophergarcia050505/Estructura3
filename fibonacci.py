from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_recursivo(n):
    if n < 2:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Muestra los primeros 10 números
for i in range(500):
    print(fibonacci_recursivo(i), end="- -")

