
# import datetime
#
# date1 = datetime.datetime(2014, 7, 2)
# date2 = datetime.datetime(2014, 7, 11)
#
# diff_days = date2 - date1
#
# print("Sample dates: " + date1.strftime("(%Y, %m, %d)") + ", " + date2.strftime("(%Y, %m, %d)"))
# print("Expected output: " + str(diff_days.days) + " days")

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)


