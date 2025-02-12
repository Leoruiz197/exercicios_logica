import timeit

def fatorial_iterativo(n):
    """Calcula o fatorial de um número de forma iterativa."""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def fatorial_recursivo(n):
    """Calcula o fatorial de um número de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)

# Entrada do usuário
num = int(input("Digite um número para calcular o fatorial: "))

# Cálculo e exibição dos resultados
print(f"Fatorial (Iterativo) de {num}: {fatorial_iterativo(num)}")
print(f"Fatorial (Recursivo) de {num}: {fatorial_recursivo(num)}")

# Comparação de tempo de execução
tempo_iterativo = timeit.timeit(lambda: fatorial_iterativo(num), number=1000)
tempo_recursivo = timeit.timeit(lambda: fatorial_recursivo(num), number=1000)

print(f"\nTempo Iterativo: {tempo_iterativo:.6f} segundos")
print(f"Tempo Recursivo: {tempo_recursivo:.6f} segundos")
