import math
a=int(input("enter the number:"))
sum=0
temp=a
while a!=0:
    sum=sum+math.factorial(a%10)
    a=a//10
print("sum is:",sum)
if sum==temp:
    print("it is strong number")
else:
    print("it is not a strong number")    