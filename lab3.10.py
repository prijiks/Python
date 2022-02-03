from collections import Counter
with open("LAB3.txt","r") as fname:
    Frequency = Counter(fname.read().split())
    print("Nuber of words =",Frequency)