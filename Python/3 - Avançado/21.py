from functools import lru_cache

# Memoization usando LRU Cache
@lru_cache(maxsize=None)
def fibonacci(n):
    """Calcula o n-ésimo número de Fibonacci usando recursão e memoization."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Entrada do usuário
n = int(input("Digite o valor de n para calcular Fibonacci: "))

# Resultado
print(f"O {n}-ésimo número de Fibonacci é: {fibonacci(n)}")
