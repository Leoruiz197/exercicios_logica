def merge_sort(arr, reverse=False):
    """Ordena um array usando Merge Sort recursivo."""
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio], reverse)
    direita = merge_sort(arr[meio:], reverse)

    return merge(esquerda, direita, reverse)

def merge(esquerda, direita, reverse):
    """Mescla duas listas ordenadas em uma única lista ordenada."""
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if (esquerda[i] < direita[j] and not reverse) or (esquerda[i] > direita[j] and reverse):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona os elementos restantes
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

# Entrada do usuário
numeros = list(map(int, input("Digite os números separados por espaço: ").split()))
ordem = input("Digite 'c' para crescente ou 'd' para decrescente: ").strip().lower()

# Define a ordem
reverse = True if ordem == 'd' else False

# Ordena e exibe o resultado
numeros_ordenados = merge_sort(numeros, reverse)
print(f"Números ordenados: {numeros_ordenados}")
