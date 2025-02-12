# Algoritmo: Cálculo do Fatorial

# Solicita ao usuário um número inteiro
num = int(input("Digite um número: "))

# Inicializa o fatorial como 1
fatorial = 1

# Calcula o fatorial usando um laço
for i in range(1, num + 1):
    fatorial *= i

# Exibe o resultado
print(f"O fatorial de {num} é: {fatorial}")
