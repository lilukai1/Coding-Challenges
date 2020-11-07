import datetime

import pytz

starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(time, timezone_string):
    timezone = pytz.timezone(timezone_string)
    rttn = time.astimezone(timezone)
    return rttn

print(to_timezone(starter, 'US/Pacific'))
