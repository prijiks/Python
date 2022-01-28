from datetime import date
name=input("What is your name?\n")
age=int(input("How old are you?\n"))
remaining_years=100-age
current_year=date.today().year
print ("Hai,",name,".HAPPY BIRTHDAY TO YOU now you are",age," years old. You will turn 100 years old in ",current_year + remaining_years) 