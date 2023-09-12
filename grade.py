a=int(input("enter the mark"))
if a>=90 and a<=100:
    print(a,"your grade is A")
elif a>=80 and a<=89:
    print(a,"your grade is B") 
elif a>=70 and a<=79:
    print(a,"your grade is C")
elif a>60 and a<=69:
    print(a,"your grade is D")
elif a>50 and a<=59:
    print(a,"your grade is E")         
else:
    print(a,"you are Failed")