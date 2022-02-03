def remove_newline(f):
    list = open(f).readlines()
    return [s.rstrip('\n')for s in list]
print(remove_newline("LAB3.txt"))   