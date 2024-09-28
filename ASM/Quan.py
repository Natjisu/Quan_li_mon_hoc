def xac_nhan_yes_no(thong_bao):
    while True:
        tra_loi = input(thong_bao + " (Yes/No): ").strip().lower()
        if tra_loi == 'yes':
            return True
        elif tra_loi == 'no':
            return False
        else:
            print("Vui lòng nhập Yes hoặc No.")


def danh_sach():
    print('Bạn đã chọn hiển thị danh sách')
    if xac_nhan_yes_no('Hiển thị danh sách không?'):
        print('Đã hiển thị ra danh sách')
    else:
        print('Không có chương trình nào được chạy!')

def tim_kiem():
    print('Bạn đã chọn tìm kiếm / lọc')
    if xac_nhan_yes_no('Xác nhận tìm kiếm / lọc không?'):
        print('Đã thực hiện chức năng tìm kiếm / lọc')
    else:
        print('Không có chương trình nào được chạy!')

def them_moi():
    print('Bạn đã chọn thêm mới')
    if xac_nhan_yes_no('Xác nhận muốn thêm mới?'):
        print('Đã thực hiện chức năng thêm mới')
    else:
        print('Không có chương trình nào được chạy!')

def cap_nhat():
    print('Bạn đã chọn chương trình cập nhật') 
    if xac_nhan_yes_no('Xác nhận chọn cập nhật?'):
        print('Đã thực hiện chức năng cập nhật') 
    else:
        print('Không có chương trình nào được chạy!')

def xoa():
    print('Bạn đã chọn chức năng xóa')
    if xac_nhan_yes_no('Xác nhận chọn xóa?'):
        print('Đã thực hiện chức năng xóa')
    else:
        print('Không có chương trình nào được chạy!')

def hien_thi_ten_sinh_vien():
    print('Bạn đã chọn hiển thị tên sinh viên')
    if xac_nhan_yes_no('Xác nhận chọn hiển thị?'):
        print('Đã thực hiện chức năng hiển thị tên sinh viên')
    else:
        print('Không có chương trình nào được chạy!')

def hien_thi_danh_sach_mon_hoc():
    print('Bạn đã chọn hiển thị danh sách môn học') 
    if xac_nhan_yes_no('Xác nhận chọn hiển thị?'):
        print('Đã thực hiện chức năng hiển thị danh sách môn học') 
    else:
        print('Không có chương trình nào được chạy!')

def so_ky_hoc():
    print('Bạn đã chọn hiển thị số kỳ học')
    if xac_nhan_yes_no('Xác nhận chọn chức năng?'):
        print('Đã thực hiện chức năng hiển thị số kỳ học')
    else:
        print('Không có chương trình nào được chạy!')

def ngay_dang_ky():
    print('Bạn đã chọn hiển thị ngày đăng ký')
    if xac_nhan_yes_no('Xác nhận chọn chức năng?'):
        print('Đã thực hiện chức năng hiển thị ngày đăng ký')
    else:
        print('Không có chương trình nào được chạy!')

def trang_thai():
    print('Bạn đã chọn hiển thị trạng thái')
    if xac_nhan_yes_no('Xác nhận chọn chức năng?'):
        print('Đã thực hiện chức năng hiển thị trạng thái')
    else:
        print('Không có chương trình nào được chạy!')



def display_menu():
    while True:
        print("\n----------Menu quản lý đăng ký học----------")
        print("1. Hiển thị danh sách")
        print("2. Tìm kiếm/Lọc")
        print("3. Thêm mới")
        print("4. Cập nhật")
        print("5. Xóa")
        print("6. Hiển thị tên sinh viên")
        print("7. Hiển thị danh sách Môn học")
        print("8. Hiển thị số Kỳ học mà sinh viên đã học")
        print("9. Hiển thị Ngày đăng ký học của sinh viên")
        print("10. Hiển thị trạng thái hiện tại của sinh viên")
        print("0. Thoát")

        try:
            lua_chon = int(input('Mời nhập lựa chọn: '))

            if lua_chon == 1:
                danh_sach()
            elif lua_chon == 2:
                tim_kiem()
            elif lua_chon == 3:
                them_moi()
            elif lua_chon == 4:
                cap_nhat()
            elif lua_chon == 5:
                xoa()
            elif lua_chon == 6:
                hien_thi_ten_sinh_vien()
            elif lua_chon == 7:
                hien_thi_danh_sach_mon_hoc()
            elif lua_chon == 8:
                so_ky_hoc()
            elif lua_chon == 9:
                ngay_dang_ky()
            elif lua_chon == 10:
                trang_thai()
            elif lua_chon == 0:
                xac_nhan = input("Bạn có chắc chắn muốn thoát chương trình? (Y/N): ").strip().upper()
                if xac_nhan == "Y":
                    print("Đã thoát chương trình")
                    break
                else:
                    print("Thoát chương trình đã bị hủy.")
            else:
                print('Lựa chọn không hợp lệ. Xin mời nhập lại!')

        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập một số từ 0 đến 10.")
