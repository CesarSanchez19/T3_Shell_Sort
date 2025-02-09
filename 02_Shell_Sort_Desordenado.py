
### Shell Sort - Desordenada  ###

# Función que implementa el algoritmo de ordenamiento Shell Sort ( Los elementos desordenados aleatoriamente diferentes lugares )

def desordenar_shell_sort(arr):

    n = len(arr)
    gap = n // 2  # Calcula el gap inicial como la mitad del tamaño del arreglo
    
    # Mientras el gap sea mayor que 0
    while gap > 0:
        # Recorre el arreglo desde la posición gap hasta el final
        for i in range(gap, n):
            # Guarda el elemento actual en una variable temporal
            temp = arr[i]
            j = i
            
            # Intercambia los elementos de manera aleatoria y no predecible
            while j >= gap and arr[j - gap] != temp:
                # Realiza el intercambio entre los elementos
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap

        # Reduce el gap a la mitad en cada iteración
        gap //= 2
    
    return arr
