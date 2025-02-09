### Shell Sort - Desordenada ###

# Función que desordena un arreglo usando una variación de Shell Sort
def shell_sort_reverse(arr):
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
            # En lugar de ordenar, intercambiamos de manera opuesta
            while j >= gap and arr[j - gap] < temp:
                # Mueve el elemento menor hacia adelante (desordena)
                arr[j] = arr[j - gap]
                # Retrocede gap posiciones
                j -= gap
            # Coloca el elemento temporal en su posición incorrecta
            arr[j] = temp
        # Reduce el gap a la mitad
        gap //= 2
    # Retorna el arreglo desordenado
    return arr
