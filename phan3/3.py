def dem_so_bon(danh_sach):
    dem = 0
    for so in danh_sach:
        if so == 4:
            dem += 1
    return dem
danh_sach = [4, 2, 4, 1, 5, 4, 7, 4]
so_lan_xuat_hien = dem_so_bon(danh_sach)
print("Số lần xuất hiện của số 4 trong danh sách là:", so_lan_xuat_hien)
