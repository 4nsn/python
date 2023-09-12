sidea=float(input("enter the side a: "))
sideb=float(input("enter the side b: "))
sidec=float(input("enter the side c: "))

squarea=sidea**2
squareb=sideb**2
squarec=sidec**2

if (squarea+squareb==squarec):
    print("it is right angled triangle")
elif (squareb+squarec==squarea):
    print("it is right angled triangle")
elif (squarea+squarec==squareb):
    print("it is right angled triangle")
else:
    print("it's not  right angled triangle")

    