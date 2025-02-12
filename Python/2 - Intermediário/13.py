# Algoritmo: Sequência de Fibonacci

# Solicita ao usuário o número de termos desejados
n = int(input("Digite quantos termos deseja: "))

# Inicializa os dois primeiros termos
a, b = 0, 1

# Gera e exibe os termos da sequência de Fibonacci
for i in range(n):
    print(a, end=" ")  # Exibe o termo sem quebrar a linha
    temp = a + b
    a = b
    b = temp

print()  # Apenas para a quebra de linha final
