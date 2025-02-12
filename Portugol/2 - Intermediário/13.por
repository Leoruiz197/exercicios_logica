algoritmo "fibonacci"
var
   n, i, a, b, temp: inteiro
inicio
   escreva("Digite quantos termos deseja: ")
   leia(n)
   a <- 0
   b <- 1
   para i de 1 ate n faca
      escreva(a, " ")
      temp <- a + b
      a <- b
      b <- temp
   fimpara
fimalgoritmo
