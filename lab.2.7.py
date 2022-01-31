dict_num={1:10, 2:10, 3:30, 4:40, 5:50, 6:60}
print("key value count")
for count,(key,value) in enumerate (dict_num.items(),1):
    print("key:",key)
    print("value:",value)
    print("count:",count)
