import time
import datetime

print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

now = datetime.datetime.now()
print(now)
# 时间偏移
new_time = datetime.timedelta(minutes=10)
print(now + new_time)

# 指定日期
one_day = datetime.datetime(2020, 8, 28)
print(one_day)
new_date = datetime.timedelta(days=8)
print(one_day + new_date)
