algoritmo "soma_digitos"
var
   num, soma, digito: inteiro
inicio
   escreva("Digite um número inteiro: ")
   leia(num)
   soma <- 0
   enquanto num > 0 faca
      digito <- num % 10
      soma <- soma + digito
      num <- num / 10
   fimenquanto
   escreva("A soma dos dígitos é: ", soma)
fimalgoritmo
