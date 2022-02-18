
from datetime import datetime, timedelta
#Add a week (7 days) and 12 hours to a given date

given_date = datetime(2020, 3, 22, 10, 0, 0)
#2020-03-29 22:00:00

newdate = given_date + timedelta(days=7, hours=12)
print(newdate)

