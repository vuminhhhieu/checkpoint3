def la_so_chan(so):
    return so % 2 == 0
def kiem_tra_chan_le():
    try:
        so_nguyen = int(input("Nhập số nguyên cần kiểm tra: "))
        if la_so_chan(so_nguyen):
            print("Số bạn vừa nhập là số chẵn.")
        else:
            print("Số bạn vừa nhập là số lẻ.")
    except ValueError:
        print("Bạn đã nhập không phải số nguyên. Vui lòng nhập lại.")
kiem_tra_chan_le()
