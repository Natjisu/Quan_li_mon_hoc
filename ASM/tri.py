def xac_nhan_yes_no(thong_bao):
    while True:
        tra_loi = input(thong_bao + " (Y/N): ").strip().lower()
        if tra_loi == 'y':
            return True
        elif tra_loi == 'n':
            return False
        else:
            print("Vui lòng nhập Y hoặc N.")

def chuc_nang_1():
    if xac_nhan_yes_no("Bạn có muốn hiển thị danh sách học kỳ không?"):
        print("Hiển thị danh sách học kỳ")

def chuc_nang_2():
    if xac_nhan_yes_no("Bạn có muốn tìm kiếm học kỳ không?"):
        print("Tìm kiếm học kỳ")

def chuc_nang_3():
    if xac_nhan_yes_no("Bạn có chắc chắn muốn thêm học kỳ không?"):
        print("Thêm học kỳ mới")

def chuc_nang_4():
    if xac_nhan_yes_no("Bạn có chắc chắn muốn cập nhật học kỳ không?"):
        print("Cập nhật thông tin học kỳ")

def chuc_nang_5():
    if xac_nhan_yes_no("Bạn có chắc chắn muốn xóa học kỳ không?"):
        print("Xóa học kỳ")

def chuc_nang_6():
    if xac_nhan_yes_no("Bạn có muốn ghi danh vào môn học trong kỳ không?"):
        print("Ghi danh vào môn học trong kỳ")

def chuc_nang_7():
    if xac_nhan_yes_no("Bạn có muốn quản lý điểm số của sinh viên không?"):
        print("Quản lý điểm số của sinh viên")

def chuc_nang_8():
    if xac_nhan_yes_no("Bạn có muốn phân bổ giảng viên cho các môn học không?"):
        print("Phân bổ giảng viên cho các môn học")

def chuc_nang_9():
    if xac_nhan_yes_no("Bạn có muốn xem lịch học không?"):
        print("Xem lịch học")

def chuc_nang_10():
    if xac_nhan_yes_no("Bạn có muốn quản lý danh sách sinh viên không?"):
        print("Quản lý danh sách sinh viên")

def kiem_tra_nhap_lieu():
    while True:
        try:
            lua_chon = int(input("Nhập số từ 1 đến 11: "))
            if 1 <= lua_chon <= 11:
                return lua_chon
            else:
                print("Số nhập không hợp lệ. Vui lòng chọn từ 1 đến 11.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

def chon_chuc_nang():
    while True:
        print('1. Hiện thị danh sách học kỳ')
        print('2. Tìm kiếm học kỳ')
        print('3. Thêm học kỳ mới')
        print('4. Cập nhật thông tin học kỳ')
        print('5. Xóa học kỳ')
        print('6. Ghi danh vào môn học trong kỳ')
        print('7. Quản lý điểm số của sinh viên')
        print('8. Phân bổ giảng viên cho các môn học')
        print('9. Xem lịch học')
        print('10. Quản lý danh sách sinh viên')
        print('11. Thoát')

        lua_chon = kiem_tra_nhap_lieu()

        if lua_chon == 1:
            chuc_nang_1()
        elif lua_chon == 2:
            chuc_nang_2()
        elif lua_chon == 3:
            chuc_nang_3()
        elif lua_chon == 4:
            chuc_nang_4()
        elif lua_chon == 5:
            chuc_nang_5()
        elif lua_chon == 6:
            chuc_nang_6()
        elif lua_chon == 7:
            chuc_nang_7()
        elif lua_chon == 8:
            chuc_nang_8()
        elif lua_chon == 9:
            chuc_nang_9()
        elif lua_chon == 10:
            chuc_nang_10()
        elif lua_chon == 11:
            if xac_nhan_yes_no("Bạn có chắc chắn muốn thoát chương trình không?"):
                print("Đang thoát chương trình...")
                break
#chon_chuc_nang()
