a=int(input("enter the number:"))
sum=0
while a!=0:
    d=a%10
    if d%2==0:
        sum=d+sum
    a=a//10
print("sum",sum)      