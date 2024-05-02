'''
Short examples on using datetime functionality in python for YouTube video
'''

import datetime

datetime_now = datetime.datetime.now()
date_now = datetime_now.date()
time_now = datetime_now.time()
weekday_now = datetime_now.weekday() # weekday starts at 0 for Sunday and ends a 6 for Saturday

print(datetime_now)
print(date_now)
print(time_now)
print(weekday_now)

# Notice that setting the day is base of 1, not 0
attack_911 = datetime.date(2001, 9, 11)
print(attack_911)

# using timedelta. Note that both must be dates or datetime. Cannot mix and match.
timedelta_since_911 = date_now - attack_911
days_since_911 = timedelta_since_911.days
whole_months_since_911 = int(days_since_911 // 30.4) # 30.4 is the average number of days in a month


print(timedelta_since_911)
print(whole_months_since_911)