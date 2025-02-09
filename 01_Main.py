from PyQt5 import QtWidgets, uic

class ShellSortApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interface.ui", self)  # Cargar la UI de Qt Designer

        # Conectar botones a funciones
        self.btnGenerate.clicked.connect(self.generar_tablas)
        self.btnSort.clicked.connect(self.ordenar)
        self.btnShuffle.clicked.connect(self.desordenar)
        self.btnClear.clicked.connect(self.borrar_datos)  # Conectar el botón para borrar datos
        self.btnReset.clicked.connect(self.reiniciar_tablas)  # Conectar el nuevo botón para reiniciar

    def generar_tablas(self):
        """Genera dos tablas con el número de filas y columnas seleccionadas."""
        filas = self.spinRows.value()
        columnas = self.spinCols.value()

        self.tableOriginal.setRowCount(filas)
        self.tableOriginal.setColumnCount(columnas)

        self.tableSorted.setRowCount(filas)
        self.tableSorted.setColumnCount(columnas)

    def obtener_datos_tabla(self):
        """Obtiene los datos de tableOriginal como una lista de números."""
        datos = []
        filas = self.tableOriginal.rowCount()
        columnas = self.tableOriginal.columnCount()

        for i in range(filas):
            for j in range(columnas):
                item = self.tableOriginal.item(i, j)
                if item and item.text().isdigit():  # Verifica si hay datos numéricos
                    datos.append(int(item.text()))

        return datos

    def actualizar_tabla(self, datos):
        """Coloca los datos ordenados/desordenados en tableSorted."""
        filas = self.tableSorted.rowCount()
        columnas = self.tableSorted.columnCount()
        index = 0

        for i in range(filas):
            for j in range(columnas):
                if index < len(datos):
                    self.tableSorted.setItem(i, j, QtWidgets.QTableWidgetItem(str(datos[index])))
                    index += 1

    def shell_sort(self, arr):
        """Ordena la lista usando Shell Sort."""
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr

    def shell_sort_reverse(self, arr):
        """Desordena la lista usando Shell Sort Inverso."""
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] < temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr

    def ordenar(self):
        """Toma los datos de tableOriginal y los ordena en tableSorted."""
        datos = self.obtener_datos_tabla()
        if datos:
            datos_ordenados = self.shell_sort(datos)
            self.actualizar_tabla(datos_ordenados)

    def desordenar(self):
        """Toma los datos de tableOriginal y los desordena en tableSorted sin usar librerías externas."""
        datos = self.obtener_datos_tabla()
        if datos:
            # Desordenar los datos de manera aleatoria mediante permutaciones sin librerías externas
            n = len(datos)
            for i in range(n):
                # Generamos un índice aleatorio en el rango de los elementos restantes
                j = i + (i % (n - i))  # Se obtiene un índice "aleatorio" simple
                # Intercambiamos los elementos
                datos[i], datos[j] = datos[j], datos[i]
            
            # Actualizamos la tabla con los datos desordenados
            self.actualizar_tabla(datos)

    def borrar_datos(self):
        """Borra todos los datos de las tablas."""
        filas = self.tableOriginal.rowCount()
        columnas = self.tableOriginal.columnCount()

        # Borra todos los elementos de tableOriginal
        for i in range(filas):
            for j in range(columnas):
                self.tableOriginal.setItem(i, j, QtWidgets.QTableWidgetItem(''))

        # Borra todos los elementos de tableSorted
        for i in range(filas):
            for j in range(columnas):
                self.tableSorted.setItem(i, j, QtWidgets.QTableWidgetItem(''))

    def reiniciar_tablas(self):
        """Elimina todas las filas y columnas de las tablas."""
        # Eliminar todas las filas y columnas de tableOriginal
        self.tableOriginal.setRowCount(0)
        self.tableOriginal.setColumnCount(0)

        # Eliminar todas las filas y columnas de tableSorted
        self.tableSorted.setRowCount(0)
        self.tableSorted.setColumnCount(0)

# Crear la aplicación y mostrar la ventana
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ShellSortApp()
    window.show()
    app.exec_()
