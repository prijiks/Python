Character="character frequency"
num={}
for n in Character:
    if n in num:
        num[n] +=1
    else:
            num[n]=1
print(num)            