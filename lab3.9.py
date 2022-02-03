with open ("LAB3.txt") as fname:
    Linecount = 0
    for line in fname:
        if Linecount != '/n':
            Linecount += 1
fname.close()
print("Total number of line is",Linecount)            