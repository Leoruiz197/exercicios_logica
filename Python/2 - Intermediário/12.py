# Algoritmo: Verificação de Número Primo

# Solicita ao usuário um número inteiro
num = int(input("Digite um número: "))

# Inicializa o contador de divisores
contador = 0

# Verifica quantos divisores o número tem
for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

# Se o número tiver exatamente dois divisores, ele é primo
if contador == 2:
    print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")
