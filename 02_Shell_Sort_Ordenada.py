def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Iniciar con la mitad del tamaño del arreglo

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:  # Desplazar elementos
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp  # Insertar en la posición correcta
        gap //= 2  # Reducir el gap

# Ejemplo de uso
datos = [8, 5, 3, 9, 2, 4]
print("Lista original:", datos)
shell_sort(datos)
print("Lista ordenada:", datos)
