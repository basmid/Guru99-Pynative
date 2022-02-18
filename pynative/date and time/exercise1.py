
#Print current date and time in Python

from datetime import datetime

now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("current date and time =", dt_string)