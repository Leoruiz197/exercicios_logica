algoritmo "fatorial"
var
   num, fatorial, i: inteiro
inicio
   escreva("Digite um número: ")
   leia(num)
   fatorial <- 1
   para i de 1 ate num faca
      fatorial <- fatorial * i
   fimpara
   escreva("O fatorial de ", num, " é: ", fatorial)
fimalgoritmo
