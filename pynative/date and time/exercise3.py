
from datetime import datetime
from datetime import timedelta
#Subtract a week (7 days)  from a given date in Python

given_date = datetime(2020, 2, 25)
#2020-02-18

new_date = given_date - timedelta(days=7)

print(new_date)
