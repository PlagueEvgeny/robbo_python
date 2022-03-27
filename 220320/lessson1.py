from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

today = date.today()
print(today)

current_time = time()
print(current_time)

now = datetime.now()
print(now)
print(now.date())
print(now.time())


three_hours = timedelta(hours=3)
print(three_hours)
three_hours = timedelta(days=1, hours=3, minutes=30, seconds=21, microseconds=1000000)
print(three_hours)
