#mijn versie
from datetime import datetime
import calendar

given_date = datetime(2020, 7, 26)
#Sunday

print(calendar.day_name[given_date.weekday()])

#site versie
# from datetime import datetime
#
# given_date = datetime(2020, 7, 26)
#
# # to get weekday as integer
# print(given_date.today().weekday())
#
# # To get the english name of the weekday
# print(given_date.strftime('%A'))
