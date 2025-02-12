# Algoritmo: Tabuada

# Solicita ao usuário um número inteiro
num = int(input("Digite um número para a tabuada: "))

# Gera e exibe a tabuada do número
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
