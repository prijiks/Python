def LastNlines(fname,N):
    with open(fname) as file:
        for line in (file.readlines()[N]):
            print(line, end='')
fname = 'LAB3.txt'  
N = 2
try:
    LastNlines(fname,N) 
except:
    print("NO FILE FOUND!")             