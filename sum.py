a=int(input("enter the number :"))
sum=10
while sum>9:
    sum=0
    while a!=0:
        sum=sum+(a%10)
        a=a//10
    a=sum
    print("sum=",sum)