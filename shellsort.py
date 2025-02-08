def shell_sort(arr):
    """Implementación del algoritmo Shell Sort"""
    n = len(arr)
    gap = n // 2  # Inicializamos el gap a la mitad del tamaño del array

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reducimos el gap a la mitad en cada iteración

    return arr
