# Algoritmo: Verificação de Número Perfeito

# Solicita ao usuário um número inteiro
num = int(input("Digite um número: "))

# Inicializa a soma dos divisores
soma = 0

# Percorre de 1 até num - 1 verificando os divisores
for i in range(1, num):
    if num % i == 0:
        soma += i

# Verifica se o número é perfeito
if soma == num:
    print(f"{num} é um número perfeito.")
else:
    print(f"{num} não é um número perfeito.")
