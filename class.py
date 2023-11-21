class Student:
    
    def nhapThongTin(self):
        self.name = str(input("Moi ban nhap ten: "))
        self.msv = str(input("Moi ban nhap ma sinh vien: "))
        self.ngaySinh = str(input("Moi ban nhap ngay sinh: "))
        self.gioiTinh = bool(input("Moi ban nhap gioi Tinh: "))
        self.tuoi = int(input("Moi ban nhap tuoi: "))
        
    def inThonTin(self):
        a = None
        if(self.gioiTinh == True):
            a = "Nam"
        else:
            a = "Nu"
        
        print("Hoc sinh nay ten la {} ".format(self.name) + " co ma sinh vien la {} ".format(self.msv) + " sinh ngay {} ".format(self.ngaySinh) +
              " gioi tinh la {} ".format(a) + " hien tai anh nay da {} ".format(self.tuoi) + "Tuoi")
        
st1 = Student()
st1.nhapThongTin()
st1.inThonTin()
