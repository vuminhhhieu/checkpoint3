def sap_xep_tang_dan(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
def main():
    danh_sach = [5, 1, 8, 92, -1, 30]
    print("Danh sách trước khi sắp xếp:", danh_sach)
    sap_xep_tang_dan(danh_sach)
    print("Danh sách sau khi sắp xếp:", danh_sach)
main()
