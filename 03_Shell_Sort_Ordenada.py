### Shell Sort - Ordenada  ###

# Función que implementa el algoritmo de ordenamiento Shell Sort ( Los elementos desordenados los ordena de menor a mayor )

def shell_sort(arr):
    # Obtiene la longitud del arreglo
    n = len(arr)
    # Calcula el gap inicial como la mitad del tamaño del arreglo
    gap = n // 2

    # Mientras el gap sea mayor que 0
    while gap > 0:
        # Recorre el arreglo desde la posición gap hasta el final
        for i in range(gap, n):
            # Guarda el elemento actual en una variable temporal
            temp = arr[i]
            j = i
            # Compara y mueve elementos que están separados por gap posiciones
            while j >= gap and arr[j - gap] > temp:
                # Mueve el elemento mayor hacia adelante
                arr[j] = arr[j - gap]
                # Retrocede gap posiciones
                j -= gap
            # Coloca el elemento temporal en su posición correcta
            arr[j] = temp
        # Reduce el gap a la mitad
        gap //= 2
    # Retorna el arreglo ordenado
    return arr