#BINARY SEARCH - PROCURAR VALORES EM LISTA

def binary_search(array, target, low, high):
    if low > high:
        return -1  # Elemento não encontrado
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, low, mid - 1)
    else:
        return binary_search(array, target, mid + 1, high)

# Dados de exemplo
array = [1, 2, 3, 4, 5]
find = 4

# Chamada da função
result = binary_search(array, find, 0, len(array) - 1)
print(f"Elemento encontrado na posição: {result}")
