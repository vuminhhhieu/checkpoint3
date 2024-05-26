def is_palindrome(chuoi):
    return chuoi == chuoi[::-1]
def kiem_tra_palindrome():
    chuoi_nhap = input("Nhập chuỗi cần kiểm tra: ")
    if is_palindrome(chuoi_nhap):
        print("Chuỗi bạn vừa nhập là palindrome.")
    else:
        print("Chuỗi bạn vừa nhập không phải là palindrome.")
kiem_tra_palindrome()
