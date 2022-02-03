import datetime
print(
    datetime.datetime.fromtimestamp(
        int("1234567890")
    ).strftime('%d-%m-%Y %H:%M:%S')
)