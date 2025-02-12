algoritmo "soma_impares"
var
   num, soma, i: inteiro
inicio
   escreva("Digite um número: ")
   leia(num)
   soma <- 0
   para i de 1 ate num faca
      se i % 2 <> 0 entao
         soma <- soma + i
      fimse
   fimpara
   escreva("A soma dos números ímpares até ", num, " é: ", soma)
fimalgoritmo
