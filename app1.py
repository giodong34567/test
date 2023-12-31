# Form implementation generated from reading ui file 'app1.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 897)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(160, 90, 871, 331))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 61, 16))
        self.label_2.setObjectName("label_2")
        self.hoVaTen = QtWidgets.QLineEdit(parent=self.groupBox)
        self.hoVaTen.setGeometry(QtCore.QRect(150, 70, 191, 20))
        self.hoVaTen.setObjectName("hoVaTen")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 61, 16))
        self.label_3.setObjectName("label_3")
        self.gioiTinh = QtWidgets.QComboBox(parent=self.groupBox)
        self.gioiTinh.setGeometry(QtCore.QRect(150, 120, 191, 22))
        self.gioiTinh.setObjectName("gioiTinh")
        self.gioiTinh.addItem("")
        self.gioiTinh.addItem("")
        self.gioiTinh.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 450, 871, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.caPhe = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.caPhe.setGeometry(QtCore.QRect(80, 50, 81, 21))
        self.caPhe.setObjectName("caPhe")
        self.bimBim = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.bimBim.setGeometry(QtCore.QRect(240, 50, 81, 21))
        self.bimBim.setObjectName("bimBim")
        self.nguoiLon = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.nguoiLon.setGeometry(QtCore.QRect(200, 130, 121, 22))
        self.nguoiLon.setObjectName("nguoiLon")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(50, 130, 131, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(50, 180, 47, 13))
        self.label_5.setObjectName("label_5")
        self.treEm = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.treEm.setGeometry(QtCore.QRect(200, 180, 121, 22))
        self.treEm.setObjectName("treEm")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(430, 130, 61, 16))
        self.label_6.setObjectName("label_6")
        self.giamGia = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.giamGia.setGeometry(QtCore.QRect(540, 130, 151, 20))
        self.giamGia.setObjectName("giamGia")
        self.tinhTien = QtWidgets.QPushButton(parent=self.centralwidget)
        self.tinhTien.setGeometry(QtCore.QRect(160, 770, 161, 51))
        self.tinhTien.setObjectName("tinhTien")
        self.tienTra = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tienTra.setGeometry(QtCore.QRect(380, 770, 261, 51))
        self.tienTra.setObjectName("tienTra")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tinhTien.clicked.connect(self.tt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ỨNG DỤNG BÁN VÉ"))
        self.groupBox.setTitle(_translate("MainWindow", "THÔNG TIN KHÁCH HÀNG"))
        self.label_2.setText(_translate("MainWindow", "HỌ VÀ TÊN:"))
        self.label_3.setText(_translate("MainWindow", "GIỚI TÍNH:"))
        self.gioiTinh.setItemText(0, _translate("MainWindow", "Nam"))
        self.gioiTinh.setItemText(1, _translate("MainWindow", "Nữ"))
        self.gioiTinh.setItemText(2, _translate("MainWindow", "Khác"))
        self.groupBox_2.setTitle(_translate("MainWindow", "DỊCH VỤ"))
        self.caPhe.setText(_translate("MainWindow", "CÀ PHÊ"))
        self.bimBim.setText(_translate("MainWindow", "BIM BIM"))
        self.label_4.setText(_translate("MainWindow", "NGƯỜI LỚN"))
        self.label_5.setText(_translate("MainWindow", "TRẺ EM"))
        self.label_6.setText(_translate("MainWindow", "GIẢM GIÁ:"))
        self.tinhTien.setText(_translate("MainWindow", "TÍNH TIỀN"))
        
    def tt(self):
        price = {
            "ca_phe" : 100000,
            "bim_bim" : 40000,
            "nguoi_lon":50000,
            "tre_em":30000
        }
        
        tienCaPhe = price["ca_phe"] if self.caPhe.isChecked() else 0
        tienBimBim = price["bim_bim"] if self.bimBim.isChecked() else 0
        tienNguoiLon = int(self.nguoiLon.text()) * price["nguoi_lon"]
        tienTreEm = int(self.treEm.text()) * price["tre_em"] 
        sum = tienCaPhe + tienBimBim + tienNguoiLon + tienTreEm
        tienGiamGia = int(self.giamGia.text()) if self.giamGia.text() != "" else 0
        sum -= tienGiamGia
        self.tienTra.setText(str(sum))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
