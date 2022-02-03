with open ("LAB3.txt") as file1,open("LAB2.txt")as file2:
    for line1, line2 in zip(file1,file2):
        print(line1+line2)