def longest_words(fname):
    with open(fname,"r") as f:
        words = f.read().split()
    max_length = len(max(words,key = len))
    return [word for word in words if len(word) == max_length]        
print(longest_words("LAB3.txt"))        