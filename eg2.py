a=int(input("enter the number:"))
b=int(input("enter the number:"))
while a!=0:
    d=a%10
    a=a//10
if b==d:
    print("yes")
else:
    print("no")
    