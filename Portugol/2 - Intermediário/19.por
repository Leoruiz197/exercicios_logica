algoritmo "mdc"
var
   a, b, temp: inteiro
inicio
   escreva("Digite dois números: ")
   leia(a, b)
   enquanto b <> 0 faca
      temp <- b
      b <- a % b
      a <- temp
   fimenquanto
   escreva("O MDC é: ", a)
fimalgoritmo
