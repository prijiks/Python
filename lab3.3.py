f = open("LAB3.txt","a")
f.write("We have added more content to the file")
f = open("LAB3.txt","r")
print(f.read())
f.close()