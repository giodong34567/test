# Form implementation generated from reading ui file 'student.ui'
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
        MainWindow.resize(1107, 884)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(150, 50, 811, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(130, 360, 871, 331))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(40, 240, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(40, 280, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(40, 80, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.hoVaTentxt = QtWidgets.QTextEdit(parent=self.groupBox)
        self.hoVaTentxt.setGeometry(QtCore.QRect(240, 40, 311, 21))
        self.hoVaTentxt.setReadOnly(True)  # Thêm dòng này để làm cho QTextEdit chỉ đọc
        self.hoVaTentxt.setObjectName("hoVaTentxt")
        self.hoVaTentxt.setObjectName("hoVaTentxt")
        self.ngaySinhtxt = QtWidgets.QTextEdit(parent=self.groupBox)
        self.ngaySinhtxt.setGeometry(QtCore.QRect(240, 80, 311, 21))
        self.ngaySinhtxt.setObjectName("ngaySinhtxt")
        self.gioiTinhtxt = QtWidgets.QTextEdit(parent=self.groupBox)
        self.gioiTinhtxt.setGeometry(QtCore.QRect(240, 120, 311, 21))
        self.gioiTinhtxt.setObjectName("gioiTinhtxt")
        self.soDienThoaitxt = QtWidgets.QTextEdit(parent=self.groupBox)
        self.soDienThoaitxt.setGeometry(QtCore.QRect(240, 160, 311, 21))
        self.soDienThoaitxt.setObjectName("soDienThoaitxt")
        self.emailtxt = QtWidgets.QTextEdit(parent=self.groupBox)
        self.emailtxt.setGeometry(QtCore.QRect(240, 200, 311, 21))
        self.emailtxt.setObjectName("emailtxt")
        self.hocPhitxt = QtWidgets.QTextEdit(parent=self.groupBox)
        self.hocPhitxt.setGeometry(QtCore.QRect(240, 250, 311, 21))
        self.hocPhitxt.setObjectName("hocPhitxt")
        self.gpaTxt = QtWidgets.QTextEdit(parent=self.groupBox)
        self.gpaTxt.setGeometry(QtCore.QRect(240, 290, 311, 21))
        self.gpaTxt.setObjectName("gpaTxt")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 720, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 720, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 720, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 0, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 21))
        self.menubar.setObjectName("menubar")
        self.menuQU_N_L_SINH_VI_N = QtWidgets.QMenu(parent=self.menubar)
        self.menuQU_N_L_SINH_VI_N.setObjectName("menuQU_N_L_SINH_VI_N")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuQU_N_L_SINH_VI_N.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Trong hàm setupUi của class Ui_MainWindow
        self.pushButton.clicked.connect(self.themSinhVien)
        self.pushButton_3.clicked.connect(self.xoaSinhVien)
        self.pushButton_2.clicked.connect(self.updateHocSinh)
        self.hienThiDuLieu()
        self.tableWidget.itemSelectionChanged.connect(self.hienThiThongTinHocSinh)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "HỌ VÀ TÊN"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NGÀY SINH"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "GIỚI TÍNH"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SỐ ĐIỆN THOẠI"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "EMAIL"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "HỌC PHÍ"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "GPA"))
        self.groupBox.setTitle(_translate("MainWindow", "ĐIỀN THÔNG TIN"))
        self.label.setText(_translate("MainWindow", "HỌ VÀ TÊN"))
        self.label_3.setText(_translate("MainWindow", "GIỚI TINH"))
        self.label_4.setText(_translate("MainWindow", "SỐ ĐIỆN THOẠI"))
        self.label_5.setText(_translate("MainWindow", "EMAIL"))
        self.label_6.setText(_translate("MainWindow", "HỌC PHÍ"))
        self.label_7.setText(_translate("MainWindow", "GPA"))
        self.label_8.setText(_translate("MainWindow", "NGÀY SINH"))
        self.pushButton.setText(_translate("MainWindow", "THÊM"))
        self.pushButton_2.setText(_translate("MainWindow", "SỬA"))
        self.pushButton_3.setText(_translate("MainWindow", "XÓA"))
        self.label_2.setText(_translate("MainWindow", "HIỂN THỊ THÔNG TIN"))
        self.menuQU_N_L_SINH_VI_N.setTitle(_translate("MainWindow", "QUẢN LÍ SINH VIÊN"))
    def themSinhVien(self):
        try:
            # Kết nối đến cơ sở dữ liệu
            db = mdb.connect(
                host="localhost",
                user="root",
                password="",  # Thay bằng mật khẩu MySQL của bạn
                database="student"
            )
            cursor = db.cursor()

            # Lấy giá trị từ các điều khiển nhập liệu trong giao diện
            ho_va_ten = self.hoVaTentxt.toPlainText()
            ngay_sinh = self.ngaySinhtxt.toPlainText()
            gioi_tinh = self.gioiTinhtxt.toPlainText()
            so_dien_thoai = self.soDienThoaitxt.toPlainText()
            email = self.emailtxt.toPlainText()
            hoc_phi = self.hocPhitxt.toPlainText()
            gpa = self.gpaTxt.toPlainText()

            # Thực hiện truy vấn SQL để thêm dữ liệu vào bảng student
            cursor.execute("INSERT INTO student (name, date, sex, phone, email, hocphi, gpa) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                                (ho_va_ten, ngay_sinh, gioi_tinh, so_dien_thoai, email, hoc_phi, gpa))

            # Lưu các thay đổi vào cơ sở dữ liệu
            db.commit()

            # Đóng kết nối
            db.close()

            # Hiển thị thông báo thành công
            msg = QtWidgets.QMessageBox()
            msg.setInformativeText("Thêm sinh viên thành công.")
            msg.exec()
            self.hienThiDuLieu()
        except Exception as e:
            # Hiển thị thông báo lỗi nếu có vấn đề xảy ra
            msg = QtWidgets.QMessageBox()
            msg.setInformativeText(f"Thêm sinh viên thất bại. Lỗi: {e}")
            msg.exec()

    def hienThiDuLieu(self):
        try:
            db = mdb.connect(
                host = "localhost",
                user = "root",
                password = "",
                database ="Student"
            )
            
            cursor = db.cursor()
            
            sql = "SELECT * FROM student"
            cursor.execute(sql)
            result = cursor.fetchall()
            
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(8)
            nam = QtWidgets.QTableWidgetItem("Nam")
            nu = QtWidgets.QTableWidgetItem("Nữ")
            for i, row in enumerate(result):
                for j, value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tableWidget.setItem(i, j, item)
            db.close()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setInformativeText(f"Hien thi that bai: {e}")
            msg.exec()
        
    def xoaSinhVien(self):
        try:
            db = mdb.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "Student"
            )
            selected_row = self.tableWidget.currentRow()
            
            student_id = self.tableWidget.item(selected_row, 0).text()
            
            cursor = db.cursor()
            
            sql = "DELETE FROM student WHERE id = %s"
            cursor.execute(sql, (student_id,))
            
            db.commit()
            
            db.close()
            self.hienThiDuLieu()
            msg = QtWidgets.QMessageBox()
            msg.setInformativeText("Xoa Thanh Cong!!!")
            msg.exec()
            
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setInformativeText(f"Xoa that bai, loi: {e}")
            msg.exec()
    def updateHocSinh(self):
        try:
            db = mdb.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "Student"          
            )
            name = self.hoVaTentxt.toPlainText()
            date = self.ngaySinhtxt.toPlainText()
            sex = self.gioiTinhtxt.toPlainText()
            phone = self.soDienThoaitxt.toPlainText()
            email = self.emailtxt.toPlainText()
            hocphi = self.hocPhitxt.toPlainText()
            gpa = self.gpaTxt.toPlainText()
            cursor = db.cursor()
            selected_row = self.tableWidget.currentRow()
            
            update_row = self.tableWidget.item(selected_row, 0).text()
            
            sql = "UPDATE student set name = %s, date = %s, sex = %s, phone = %s, email = %s, hocphi = %s, gpa = %s where id = %s"
            cursor.execute(sql, (name, date, sex, phone, email, hocphi, gpa, update_row))
            
            db.commit()
            
            db.close()
            self.hienThiDuLieu()
            msg = QtWidgets.QMessageBox()
            msg.setInformativeText("Cap nhat Thanh Cong")
            msg.exec()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setInformativeText(f"Cap nhat that bai, loi: {e}")
            msg.exec()
    
    def hienThiThongTinHocSinh(self):
        try:
            selected_row = self.tableWidget.currentRow()
            
            hoVaTen = self.tableWidget.item(selected_row, 1).text()
            ngaySinh = self.tableWidget.item(selected_row, 2).text()
            gioiTinh = self.tableWidget.item(selected_row, 3).text()
            soDienThoai = self.tableWidget.item(selected_row, 4).text()
            email = self.tableWidget.item(selected_row, 5).text()
            hocPhi = self.tableWidget.item(selected_row, 6).text()
            gpa = self.tableWidget.item(selected_row, 7).text()
            
            self.hoVaTentxt.setPlainText(hoVaTen)
            self.ngaySinhtxt.setPlainText(ngaySinh)
            self.gioiTinhtxt.setPlainText(gioiTinh)
            self.soDienThoaitxt.setPlainText(soDienThoai)
            self.emailtxt.setPlainText(email)
            self.hocPhitxt.setPlainText(hocPhi)
            self.gpaTxt.setPlainText(gpa)
            
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setInformativeText("Chọn thất bại, lỗi : {e}")
            msg.exec()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
