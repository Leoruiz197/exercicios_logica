algoritmo "contagem_digitos"
var
   num, contador: inteiro
inicio
   escreva("Digite um número inteiro: ")
   leia(num)
   contador <- 0
   enquanto num <> 0 faca
      num <- num / 10
      contador <- contador + 1
   fimenquanto
   escreva("O número tem ", contador, " dígitos.")
fimalgoritmo
