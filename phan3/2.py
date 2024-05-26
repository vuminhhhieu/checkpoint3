from datetime import datetime
date1 = datetime(2014, 7, 2)
date2 = datetime(2014, 7, 11)
delta = date2 - date1
print("Số ngày giữa hai ngày:", delta.days)