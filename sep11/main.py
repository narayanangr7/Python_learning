# STOP 1 : GETTING A INPUT FROM the user
a=int (input("enter your number"))
print(a)
b=int (input("enter your number"))
print(b)
if a%2 == 0:
    print("even")
else:
    print("add")   
if b%2 == 0:
    print("even")
else:
    print("add")   
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a!=b)
print(a==b)

#=======================================

n= int(input("enter your number of year  :"))
if  n>=2001 and n<=2100:
    print("21st Century")
else :
    print("not 21st Century") 


a= int(input("enter the number "))
b= int(input("enter the number "))
c=a+b
if c%5 ==0:
    print(1)
else:
    print(0)

# =========================================
n= int(input("enter the number "))
if n%7 ==0:
    print("yes")
else:
    print("no")    

# =========================================

n= int(input("enter the food amount "))
if n>500 :
    print("free delivery",n)
else:
    print("charged",n+50)
