from datetime import date, timedelta
currdat = date.today()
duedat = date.today()-timedelta(5)
print("Five days from current date ",duedat)