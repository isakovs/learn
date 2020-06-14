from datetime import date, time, datetime, timedelta
date = date(2020, 6, 7)
print(date)

strdatetime = '01/01/17 12:10:03.234567'
final_time = datetime.strptime(strdatetime, '%d/%m/%y %H:%M:%S.%f')
print(final_time)
