a=int(input("Enter your number"))
b=int(input("Enter your number"))
c=int(input("Enter your number"))
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
elif c>b and c>a:
    print(c)
elif a==b==c:
    print(a)