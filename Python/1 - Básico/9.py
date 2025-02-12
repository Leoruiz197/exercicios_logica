# Algoritmo: Calculadora Simples

# Solicita ao usuário dois números reais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operador = input("Digite a operação (+, -, *, /): ")

# Realiza a operação escolhida
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero!")
        exit()
else:
    print("Operador inválido!")
    exit()

# Exibe o resultado
print("Resultado:", resultado)
