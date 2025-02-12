# Algoritmo: Soma dos Dígitos

# Solicita ao usuário um número inteiro
num = int(input("Digite um número inteiro: "))

# Inicializa a soma dos dígitos
soma = 0

# Calcula a soma dos dígitos
while num > 0:
    digito = num % 10  # Obtém o último dígito
    soma += digito  # Adiciona o dígito à soma
    num //= 10  # Remove o último dígito

# Exibe o resultado
print("A soma dos dígitos é:", soma)
