# Função para ordenar um vetor de inteiros em ordem crescente usando o algoritmo de seleção.
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Função para ordenar um vetor de inteiros em ordem crescente ou decrescente.
def custom_sort(arr, reverse=False):
    arr.sort(reverse=reverse)

# Função para encontrar o elemento máximo em um vetor de inteiros não ordenado.
def find_max(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

# Função para encontrar o elemento mínimo em um vetor de inteiros não ordenado.
def find_min(arr):
    min_element = arr[0]
    for num in arr:
        if num < min_element:
            min_element = num
    return min_element

# Função para encontrar o segundo menor número em um vetor de inteiros.
def find_second_smallest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    if len(unique_arr) < 2:
        return None
    return unique_arr[1]

# Função para remover elementos duplicados de um vetor de inteiros.
def remove_duplicates(arr):
    return list(set(arr))

# Função para contar números pares e ímpares em um vetor ordenado.
def count_even_odd(arr):
    even_count = sum(1 for num in arr if num % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count

# Função para encontrar o terceiro maior número em um vetor de inteiros.
def find_third_largest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort(reverse=True)
    if len(unique_arr) < 3:
        return None
    return unique_arr[2]

# Função para calcular a mediana de um vetor de inteiros.
def find_median(arr):
    arr.sort()
    middle_index = len(arr) // 2
    if len(arr) % 2 == 1:
        return arr[middle_index]
    else:
        return (arr[middle_index - 1] + arr[middle_index]) / 2.0

# Exemplo de uso das funções:
if __name__ == "__main__":
    vetor = [4, 2, 9, 1, 5, 7, 3, 8, 6]

    selection_sort(vetor)
    print("Vetor ordenado (crescente):", vetor)

    custom_sort(vetor, reverse=True)
    print("Vetor ordenado (decrescente):", vetor)

    max_element = find_max(vetor)
    print("Maior elemento:", max_element)

    min_element = find_min(vetor)
    print("Menor elemento:", min_element)

    second_smallest = find_second_smallest(vetor)
    print("Segundo menor número:", second_smallest)

    unique_vetor = remove_duplicates(vetor)
    print("Vetor sem duplicatas:", unique_vetor)

    even_count, odd_count = count_even_odd(vetor)
    print("Quantidade de números pares:", even_count)
    print("Quantidade de números ímpares:", odd_count)

    third_largest = find_third_largest(vetor)
    print("Terceiro maior número:", third_largest)

    median = find_median(vetor)
    print("Mediana:", median)
