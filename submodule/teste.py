import datetime

now = datetime.datetime.now()

d1 = datetime.datetime(now.year,now.month-11,now.day)

print(now-d1)
print((5-10)%12)