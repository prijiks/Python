import random 
def random_line(f):
    line = open(f).read().splitlines()
    return random.choice(line)
print(random_line("LAB3.txt"))   