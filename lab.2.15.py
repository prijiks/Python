import string
import random
import string

Lower = string.ascii_lowercase
Upper = string.ascii_uppercase
Number = string.digits
Symbols = string.punctuation
Passwordlength = 10
Total=Lower+Upper+Number+Symbols
Password = "".join(random.sample(Total,Passwordlength))
print(Password)
