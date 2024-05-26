def tinh_giai_thua(n):
    if n == 0:
        return 1
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua
def main():
    try:
        so_nguyen = int(input("Nhập số nguyên cần tính giai thừa: "))
        if so_nguyen < 0:
            print("Không thể tính giai thừa của số nguyên âm.")
        else:
            ket_qua = tinh_giai_thua(so_nguyen)
            print(f"Giai thừa của {so_nguyen} là: {ket_qua}")
    except ValueError:
        print("Bạn đã nhập không phải số nguyên. Vui lòng nhập lại.")
main()
