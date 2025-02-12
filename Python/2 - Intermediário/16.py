# Algoritmo: Cálculo da Média Ponderada

# Solicita ao usuário três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Solicita os pesos correspondentes
peso1 = float(input("Digite o peso da primeira nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))
peso3 = float(input("Digite o peso da terceira nota: "))

# Calcula a média ponderada
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Exibe o resultado
print("A média ponderada é:", media)
