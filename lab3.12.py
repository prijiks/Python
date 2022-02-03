List = ["Apple", "Orange", "Grapes", "Pineapple"]
with open("LAB3.txt","w") as fname:
 for element in List:
     fname.write(element +"\n")
content = open("LAB3.txt")
print(content.read())
fname.close()    