import collections
string = input("Enter a string:")
frequencies = collections.Counter(string)
repeated = {}
for key,value in frequencies.items():
    if value > 1:
      repeated[key] = value
print(repeated)    