a=int(input("enter the number:"))
sum=0
pro=1
temp=a
while a!=0:
    sum =sum+(a%10)
    a=a//10
print("sum is",sum)
while temp!=0:
    pro=pro*(temp%10)
    temp=temp//10
print("product is",pro)
if sum==pro:
    print("it is spy number")
else:
    print("it is not a spy number")