def xacnhan(thong_bao):
    while True:
        tra_loi = input(thong_bao + " (Y/N): ").strip().lower()
        if tra_loi == 'y':
            return True
        elif tra_loi == 'n':
            return False
        else:
            print("Vui lòng nhập Y hoặc N.")
def chuc_nang_1():
    if xacnhan("Bạn có muốn hiển thị danh sách sinh viên không? "):
        print("Đã chọn chương trình: Hiển thị danh sách")
def chuc_nang_2():
    if xacnhan("Bạn có muốn tìm kiếm sinh viên không? "):
        print("Đã chọn chương trình: Tìm kiếm ")
def chuc_nang_3():
    if xacnhan("Bạn có muốn thêm sinh viên mới không? "):
        print("Đã chọn chương trình: Thêm mới")
    print("Đã thêm sinh viên thành công.")
def chuc_nang_4():
    if xacnhan("Bạn có muốn cập nhật sinh viên không? "):
        print("Đã chọn chương trình: Cập nhật")
def chuc_nang_5():
    if xacnhan("Bạn có muốn xóa sinh viên không? "):
        print("Đã chọn chương trình: Xóa")
def chuc_nang_6():
    if xacnhan("Bạn có muốn sắp xếp sinh viên không? "):
        print("Đã chọn chương trình: Sắp xếp")
def chuc_nang_7():
    if xacnhan("Bạn có muốn tìm kiếm sinh viên theo tháng không? "):
        print("Đã chọn chương trình: Thống kê sinh viên theo chuyên ngành")
def chuc_nang_8():
    if xacnhan("Bạn có muốn tìm kiếm sinh viên theo chuyên ngành? "):
        print("Đã chọn chương trình: Tìm kiếm sinh viên theo chuyên ngành")
def chuc_nang_9():
    if xacnhan("Bạn có muốn tìm kiếm sinh viên theo ngày sinh không? "):
        print("Đã chọn chương trình: Tìm kiếm sinh viên theo ngày sinh")
def chuc_nang_10():
    if xacnhan("Bạn có muốn tìm kiếm sinh viên theo năm sinh không? "):
        print("Đã chọn chương trình: Tìm kiếm sinh viên theo năm sinh")
def chuc_nang_11():
    if xacnhan("Bạn có muốn thoát chương trình không?"):
        print("Bạn đã thoát chương trình.")
        exit(0)
    else:
        print('Không thoát chương trình')

def display_menu():
    while True:
        print("\nQUẢN LÝ CHUYÊN NGÀNH")
        print("1. Hiển thị danh sách")
        print("2. Tìm kiếm Mã")
        print("3. Thêm mới Tên")
        print("4. Cập nhật ngày bắt đầu")
        print("5. Xóa sinh viên")
        print("6. Sắp xếp theo tên")
        print("7. Xuất dữ liệu năm học")
        print("8. Tìm kiếm mô tả ngành")
        print("9. Thống kê số lượng sinh viên")
        print("10. hiển thị sinh viên học theo chuyên ngành")
        print("0. Thoát")
    
        try:
            chon = int(input("Mời nhập chương trình: "))
            
            if chon == 1:
                chuc_nang_1()
                
            elif chon == 2:
                chuc_nang_2()
                
            elif chon == 3:
                chuc_nang_3()

            elif chon == 4:
                chuc_nang_4()

            elif chon == 5:
                chuc_nang_5()

            elif chon == 6:
                chuc_nang_6()

            elif chon == 7:
                chuc_nang_7()

            elif chon ==8:
                chuc_nang_8()

            elif chon == 9:
                chuc_nang_9()

            elif chon == 10:
                chuc_nang_10()
    
            elif chon == 0:
                xac_nhan = input("Bạn có chắc chắn muốn thoát chương trình? (Y/N): ").strip().upper()
                if xac_nhan == "Y":
                    print("Đã thoát chương trình")
                    break
                else:
                    print("Thoát chương trình đã bị hủy.")

                
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập từ 0 đến 10.")
                
        except ValueError:
            print("Lựa chọn không hợp lệ,không được nhập ký tự, vui lòng thử lại đúng yêu cầu(0-10)")