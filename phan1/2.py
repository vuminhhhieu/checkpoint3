import math
def cal_area(ban_kinh):
    return math.pi * ban_kinh**2
def main():
    try:
        ban_kinh = float(input("Nhập bán kính của hình tròn (đơn vị): "))
        if ban_kinh <= 0:
            print("Bán kính phải lớn hơn 0.")
        else:
            dien_tich = cal_area(ban_kinh)
            print("Diện tích của hình tròn là:", dien_tich)
    except ValueError:
        print("Bạn đã nhập không phải số. Vui lòng nhập lại.")
main()
