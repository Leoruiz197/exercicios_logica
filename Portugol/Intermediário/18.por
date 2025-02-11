algoritmo "palindromo"
var
   palavra, reverso: caractere
   i: inteiro
inicio
   escreva("Digite uma palavra: ")
   leia(palavra)
   reverso <- ""
   para i de comprimento(palavra) ate 1 passo -1 faca
      reverso <- reverso + palavra[i]
   fimpara
   se palavra = reverso entao
      escreva("É um palíndromo.")
   senao
      escreva("Não é um palíndromo.")
   fimse
fimalgoritmo
