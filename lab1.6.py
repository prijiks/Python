def isPalindrome(string):
    return string == string [::-1]
s=str(input("Enter a string:")).upper() 
ans=isPalindrome(s)   
if ans:
    print("Yes,{} is a Palindrome.".format(s))
else:
    print("No,{} is not a Palindrome.".format(s))    