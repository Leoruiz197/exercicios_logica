# Algoritmo: Cálculo do MDC (Máximo Divisor Comum)

# Solicita ao usuário dois números inteiros
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

# Algoritmo de Euclides para calcular o MDC
while b != 0:
    temp = b
    b = a % b
    a = temp

# Exibe o resultado
print("O MDC é:", a)
