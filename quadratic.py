import math
a=int(input("enter the number a: "))
b=int(input("enter the number b: "))
c=int(input("enter the number c: "))

d=b**2-4*a*c
6
if d>0:
    root1=(-b + math.sqrt(d)) / 2*a
    root2=(-b - math.sqrt(d)) / 2*a
elif d==0:
    root1=root2=(-b / (2*a)) 
else:
    root1=(-b / (2*a)) + (math.sqrt(-d) / 2*a)
    root2=(-b / (2*a)) - (math.sqrt(-d) / 2*a)
    
print(root1,"is root 1")
print(root2,"is root 2")    