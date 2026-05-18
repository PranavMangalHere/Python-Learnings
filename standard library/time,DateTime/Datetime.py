import datetime

# d = datetime.date(2016, 7, 24)
# print(d)

tday = datetime.date.today()
# # print(tday)

# tdelta = datetime.timedelta(days = 7)

# print(tday - tdelta)

bday = datetime.date(2005, 4, 11)

till_day = bday - tday
print(till_day.days)

