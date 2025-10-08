x=int(input("Enter your number"))
y=int(input("Enter your number"))
if x>0 and y>0:
    print("Quadrant 1")
elif x<0 and y>0:
    print("Quadrant 2")
elif x<0 and y<0:
    print("Quadrant 3")
elif x>0 and y<0:
    print("Quadrant 4")
elif x==0 and y==0:
    print("center")
else :
    print("Invalid")