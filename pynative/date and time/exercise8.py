from datetime import datetime

given_date = datetime(2020, 2, 25)

#"2020-02-25 00:00:00"

str = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(str)

