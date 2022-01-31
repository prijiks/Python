List =[10,20,30,40,50]
def Sublist(List):
   Sublist = [[]]
   for i in range (len(List)+1):
        for n in range (i):
         Sublist.append(List[n:i])
print(Sublist(List))        