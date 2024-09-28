def hien_thi():
    xac_nhan = input("Bạn có chắc chắn muốn hiển thị danh sách? (Y/N): ").strip().upper()
    if xac_nhan == "Y":
        print("Đã chọn chương trình: Hiển thị danh sách")
    else:
        print("Hiển thị danh sách đã bị hủy.")

def tim_kiem():
    xac_nhan = input("Bạn có chắc chắn muốn tìm kiếm hoặc lọc? (Y/N): ").strip().upper()
    if xac_nhan == "Y":
        print("Đã chọn chương trình: Tìm kiếm")
    else:
        print("Tìm kiếm đã bị hủy.")

def them_moi():
    xac_nhan = input("Bạn có chắc chắn muốn thêm mới? (Y/N): ").strip().upper()
    if xac_nhan == "Y":
        print("Đã chọn chương trình: Thêm mới")
    else:
        print("Thêm mới đã bị hủy.")

def cap_nhat():
    xac_nhan = input("Bạn có chắc chắn muốn cập nhật? (Y/N): ").strip().upper()
    if xac_nhan == "Y":
        print("Đã chọn chương trình: Cập nhật")
    else:
        print("Cập nhật đã bị hủy.")

def xoa():
    xac_nhan = input("Bạn có chắc chắn muốn xóa? (Y/N): ").strip().upper()
    if xac_nhan == "Y":
        print("Đã chọn chương trình: Xóa")
    else:
        print("Xóa đã bị hủy.")

def sap_xep():
    xac_nhan = input("Bạn có chắc chắn muốn sắp xếp? (Y/N): ").strip().upper()
    if xac_nhan == "Y":
        print("Đã chọn chương trình: Sắp xếp")
    else:
        print("Sắp xếp đã bị hủy.")

def phan_trang():
    xac_nhan = input("Bạn có chắc chắn muốn phân trang? (Y/N): ").strip().upper()
    if xac_nhan == "Y":
        print("Đã chọn chương trình: Phân trang")
    else:
        print("Phân trang đã bị hủy.")

def xem_chi_tiet():
    xac_nhan = input("Bạn có chắc chắn muốn xem chi tiết? (Y/N): ").strip().upper()
    if xac_nhan == "Y":
        print("Đã chọn chương trình: Xem chi tiết")
    else:
        print("Xem chi tiết đã bị hủy.")

def xuat_du_lieu():
    xac_nhan = input("Bạn có chắc chắn muốn xuất dữ liệu? (Y/N): ").strip().upper()
    if xac_nhan == "Y":
        print("Đã chọn chương trình: Xuất dữ liệu")
    else:
        print("Xuất dữ liệu đã bị hủy.")

def phuc_hoi_du_lieu():
    xac_nhan = input("Bạn có chắc chắn muốn phục hồi dữ liệu? (Y/N): ").strip().upper()
    if xac_nhan == "Y":
        print("Đã chọn chương trình: Phục hồi dữ liệu")
    else:
        print("Phục hồi dữ liệu đã bị hủy.")

def menu():
    while True:
        print("\n --------- QUẢN LÝ MÔN HỌC ----------")
        print("1. Hiển thị danh sách")
        print("2. Tìm kiếm hoặc lọc")
        print("3. Thêm mới ")
        print("4. Cập nhật")
        print("5. Xóa")
        print("6. Sắp xếp")
        print("7. Phân trang")
        print("8. Xem chi tiết")
        print("9. Xuất dữ liệu")
        print("10. Phục hồi dữ liệu")
        print("0. Thoát")

        try:
            chon = int(input("Mời nhập chương trình: "))

            if chon == 1:
                hien_thi()
                
            elif chon == 2:
                tim_kiem()

            elif chon == 3:
                them_moi()

            elif chon == 4:
                cap_nhat()

            elif chon == 5:
                xoa()

            elif chon == 6:
                sap_xep()

            elif chon == 7:
                phan_trang()

            elif chon == 8:
                xem_chi_tiet()

            elif chon == 9:
                xuat_du_lieu()

            elif chon == 10:
                phuc_hoi_du_lieu()

            elif chon == 0:
                xac_nhan = input("Bạn có chắc chắn muốn thoát chương trình? (Y/N): ").strip().upper()
                if xac_nhan == "Y":
                    print("Đã thoát chương trình")
                    break
                else:
                    print("Thoát chương trình đã bị hủy.")

            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.")

        except ValueError:
            print("Lựa chọn không hợp lệ, không được nhập ký tự, vui lòng thử lại đúng yêu cầu(1-5)")

