from random import randint
length=int(input("Enter the length of password: "))
print("The password is : ",end='')
r=''
for i in range(length):
    k=randint(33,126)
    r+=chr(k)
print(r)