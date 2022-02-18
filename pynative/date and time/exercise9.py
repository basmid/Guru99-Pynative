from datetime import datetime
from dateutil.relativedelta import relativedelta

#Calculate the date 4 months from the current date
given_date = datetime(2020, 2, 25).date()

#2020-06-25

six_months = given_date + relativedelta(months=+4)
print(six_months)
