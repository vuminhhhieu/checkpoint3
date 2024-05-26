def reverse_str(string):
    return string[::-1]
def dao_nguoc_noi_dung():
    chuoi_nhap = input("Nhập nội dung cần đảo ngược: ")
    chuoi_dao_nguoc = reverse_str(chuoi_nhap)
    print("Nội dung sau khi đảo ngược:", chuoi_dao_nguoc)
dao_nguoc_noi_dung()
