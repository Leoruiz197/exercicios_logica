# Algoritmo: Verificação de Palíndromo

# Solicita ao usuário uma palavra
palavra = input("Digite uma palavra: ")

# Inverte a palavra usando slicing
reverso = palavra[::-1]

# Verifica se é um palíndromo
if palavra == reverso:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
