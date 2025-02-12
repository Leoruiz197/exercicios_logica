algoritmo "numero_primo"
var
   num, i, contador: inteiro
inicio
   escreva("Digite um número: ")
   leia(num)
   contador <- 0
   para i de 1 ate num faca
      se num % i = 0 entao
         contador <- contador + 1
      fimse
   fimpara
   se contador = 2 entao
      escreva(num, " é primo.")
   senao
      escreva(num, " não é primo.")
   fimse
fimalgoritmo
