import sys
from PyQt5 import QtWidgets, uic
from shellsort import shell_sort  # Importamos el algoritmo de ordenamiento


class ShellSortApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("shellsort.ui", self)  # Cargar la interfaz desde el archivo .ui

        # Verificar que los botones están correctamente conectados
        try:
            self.btnOrdenar.clicked.connect(self.ordenar_datos)
        except AttributeError:
            print("Error: El botón 'btnOrdenar' no se encuentra en el archivo .ui.")
        
        try:
            self.btnConfigurar.clicked.connect(self.configurar_tabla)
        except AttributeError:
            print("Error: El botón 'btnConfigurar' no se encuentra en el archivo .ui.")

    def configurar_tabla(self):
        """Configura el número de filas y columnas según lo seleccionado en los QSpinBox."""
        filas = self.spinFilas.value()
        columnas = self.spinColumnas.value()
        self.tableWidget.setRowCount(filas)
        self.tableWidget.setColumnCount(columnas)

    def ordenar_datos(self):
        """Obtiene los datos de la tabla, los ordena con Shell Sort y los vuelve a mostrar."""
        filas = self.tableWidget.rowCount()
        columnas = self.tableWidget.columnCount()

        datos = []
        for fila in range(filas):
            for columna in range(columnas):
                item = self.tableWidget.item(fila, columna)
                if item is not None and item.text().isdigit():  # Solo tomar números
                    datos.append(int(item.text()))

        if not datos:
            return  # No hacer nada si la tabla está vacía

        datos_ordenados = shell_sort(datos)  # Ordenar los datos

        # Insertar los datos ordenados en la tabla (en orden de fila por columna)
        index = 0
        for fila in range(filas):
            for columna in range(columnas):
                if index < len(datos_ordenados):
                    self.tableWidget.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(datos_ordenados[index])))
                    index += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = ShellSortApp()
    ventana.show()
    sys.exit(app.exec_())
