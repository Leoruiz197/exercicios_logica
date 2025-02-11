algoritmo "ordenacao_simples"
var
   a, b, c, temp: inteiro
inicio
   escreva("Digite três números: ")
   leia(a, b, c)
   
   se a > b entao
      temp <- a
      a <- b
      b <- temp
   fimse
   se a > c entao
      temp <- a
      a <- c
      c <- temp
   fimse
   se b > c entao
      temp <- b
      b <- c
      c <- temp
   fimse

   escreva("Números em ordem crescente: ", a, ", ", b, ", ", c)
fimalgoritmo
