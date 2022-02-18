
from datetime import datetime
#Day_name  Day_number  Month_name  Year

given_date = datetime(2020, 2, 25)
#Tuesday 25 February 2020

new_date = given_date.strftime('%A %d %B %Y')
print(new_date)

