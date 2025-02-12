# Algoritmo: Ordenação Simples

# Solicita ao usuário três números inteiros
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

# Ordenação dos números usando troca de valores
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

# Exibe os números em ordem crescente
print("Números em ordem crescente:", a, ",", b, ",", c)
