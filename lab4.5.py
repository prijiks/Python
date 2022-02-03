from datetime import date
Date1 = date(2000,2,28)
Date2 = date(2001,2,28)
Date3 = Date2 - Date1
print(abs(Date3.days))
