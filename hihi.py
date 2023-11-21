from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 400, 300)
        self.tableWidget.setColumnCount(4)

        # Thêm một hàng từ cơ sở dữ liệu (ví dụ)
        result = [(1, 'John', 25, 'A')]
        self.addRowFromDatabase(result)

        # Thêm một hàng thủ công
        manual_data = ['Alice', 'Doe', 22, 'B']
        manual_data1 = ['Alice', 'Doe', 22, 'B']
        self.addRowManually(manual_data)
        self.addRowManually(manual_data1)
        self.show()

    def addRowFromDatabase(self, result):
        for i, row in enumerate(result):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(i, j, item)

    def addRowManually(self, data):
        rowPosition = self.tableWidget.rowCount()
        print(rowPosition)
        self.tableWidget.insertRow(rowPosition)

        for i, value in enumerate(data):
            item = QtWidgets.QTableWidgetItem(str(value))
            self.tableWidget.setItem(rowPosition, i, item)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWindow()
    app.exec_()
