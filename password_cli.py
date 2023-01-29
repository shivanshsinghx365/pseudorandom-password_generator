from random import randint
length=int(input("Enter the length of password: "))
print("The password is : ",end='')
password=''
for i in range(length):
    k=randint(33,126)      #ensures that k is a writeable ASCII character
    password+=chr(k)
print(password)
