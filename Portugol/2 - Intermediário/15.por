algoritmo "numero_perfeito"
var
   num, i, soma: inteiro
inicio
   escreva("Digite um número: ")
   leia(num)
   soma <- 0
   para i de 1 ate num - 1 faca
      se num % i = 0 entao
         soma <- soma + i
      fimse
   fimpara
   se soma = num entao
      escreva(num, " é um número perfeito.")
   senao
      escreva(num, " não é um número perfeito.")
   fimse
fimalgoritmo
