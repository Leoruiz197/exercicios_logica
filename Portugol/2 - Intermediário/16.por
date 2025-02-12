algoritmo "media_ponderada"
var
   nota1, nota2, nota3, peso1, peso2, peso3, media: real
inicio
   escreva("Digite três notas: ")
   leia(nota1, nota2, nota3)
   escreva("Digite os pesos correspondentes: ")
   leia(peso1, peso2, peso3)
   media <- (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
   escreva("A média ponderada é: ", media)
fimalgoritmo
