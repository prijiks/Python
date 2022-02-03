def sum (num):
    if num <1:
        return 0
    else:
        return num +sum(num-2)
print(sum(2)) 
print(sum(4))          