# Algoritmo: Soma dos Números Ímpares

# Solicita ao usuário um número inteiro
num = int(input("Digite um número: "))

# Inicializa a soma
soma = 0

# Percorre os números de 1 até num e soma os ímpares
for i in range(1, num + 1):
    if i % 2 != 0:
        soma += i

# Exibe o resultado
print(f"A soma dos números ímpares até {num} é: {soma}")
