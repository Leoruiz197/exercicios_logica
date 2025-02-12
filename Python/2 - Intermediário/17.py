# Algoritmo: Contagem de Dígitos

# Solicita ao usuário um número inteiro
num = int(input("Digite um número inteiro: "))

# Inicializa o contador de dígitos
contador = 0

# Conta os dígitos do número
while num != 0:
    num //= 10  # Usa divisão inteira para remover o último dígito
    contador += 1

# Exibe o resultado
print("O número tem", contador, "dígitos.")
