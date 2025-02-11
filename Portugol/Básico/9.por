algoritmo "calculadora"
var
   num1, num2, resultado: real
   operador: caractere
inicio
   escreva("Digite dois números: ")
   leia(num1, num2)
   escreva("Digite a operação (+, -, *, /): ")
   leia(operador)
   se operador = "+" entao
      resultado <- num1 + num2
   senao se operador = "-" entao
      resultado <- num1 - num2
   senao se operador = "*" entao
      resultado <- num1 * num2
   senao se operador = "/" entao
      se num2 <> 0 entao
         resultado <- num1 / num2
      senao
         escreva("Erro: divisão por zero!")
         pare
      fimse
   senao
      escreva("Operador inválido!")
      pare
   fimse
   escreva("Resultado: ", resultado)
fimalgoritmo
