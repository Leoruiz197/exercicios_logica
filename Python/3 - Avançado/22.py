def quick_sort(arr, reverse=False):
    """Implementação do Quick Sort com opção de ordenação reversa."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Escolhe o pivô como o elemento central
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    sorted_list = quick_sort(left, reverse) + middle + quick_sort(right, reverse)

    return sorted_list[::-1] if reverse else sorted_list

# Entrada do usuário
arr = list(map(int, input("Digite os números separados por espaço: ").split()))
order = input("Digite 'c' para crescente ou 'd' para decrescente: ").strip().lower()

# Define a ordem
reverse = True if order == 'd' else False

# Ordena e exibe o resultado
sorted_arr = quick_sort(arr, reverse)
print(f"Números ordenados: {sorted_arr}")
