num=int(input("Choose a number to divide:"))
divisor_list=[]
for i in range (1,num+1):
    if num % i==0:
        divisor_list.append(i)
print("List of all the divisors of {0} is {1}".format(num,divisor_list))        
