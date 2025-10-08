X = int(input("Enter your marks: "))

match X:
    case x if x >= 80 and x<= 100:
        print("A")
    case x if x >= 60  and x<= 79:
        print("B")
    case x if x >= 50  and x<= 59:
        print("C")
    case x if x >= 40  and x<= 49:
        print("D")
    case x if x < 40:
        print("Fail")
    case _:
        print("Invalid marks")
# Read two numbers from input
#=================================================
1,
N=int(input("enter your number"))
M=int(input("enter your number"))
total = N + M
if total % 2 == 0:
    print("even")
else:
    print("odd")

#=================================================

# 2)  
n = int(input())
a = n // 10  
b = n % 10   
m = a + b
j = a * b
if m + j == n:
    print("Great")
else:
    print("No")
# #=========================================================

#3) 
cons = input()
unit = int(input())
#condition
if cons == "residential":
    if unit > 0 and unit <= 100:
        print(cons,(3*unit))
    elif unit >= 101 and unit <= 200:
        print(cons,(5*unit))
    elif unit > 200:
        print(cons,(7*unit))
    else:
        print("Invalid unit")
elif cons == "commercial":
    if unit > 0 and unit <= 100:
        print(cons,(5*unit))
    elif unit > 100 and unit <= 200:
        print(cons,(7*unit))
    elif unit > 200:
        print(cons,(10*unit))
    else:
        print("Invalid unit")

#======================================

#8 question

s=int(input("enter you timeing"))
if s >= 9 and s<=12:
    print("morning show")
elif s >12 and s <=16:
    print("matinee show")
elif s >16 and s<=20:
    print("evening show")
elif s>20 and s<=24:
    print("night show")

#==========================================

#9 question

# 9) # given
d = float(input("Enter the distance in km"))
choice = input("Enter the Conversion")
# Condition - (Conversion)
match choice:
    case "meter":
        print(d*1000,"m")
    case "centimeter":
        print(d*100000,"cm")
    case "millimeter":
        print(d*1000000,"mm")
    case "miles":
        print(d*0.621371,"miles")
    case _ :
        print("Invalid Conversion")
# 10) #given
pm = (input())
#condition
if pm == "UPI":
    print("You selected UPI payment")
elif pm == "Card":
    print( "You selected Debit/Credit Card payment")
elif pm == "Net Banking":
    print("You selected Net Banking")
elif pm == "COD":
    print("You selected Cash on Delivery")
else:
    print("Invalid Payment Mode")


# # ===========================================
# #5 question

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c and c == a:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")



# 6 question

a = int(input('Enter a number = '))
if a % 3 == 0 and a % 5 == 0:
    print('FizzBuzz')
elif a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')
else:
    print('The number is not divisible')


# 7 question

e = input('Enter a course (Science / Commerce / Arts ) = ')
match e:
    case 'Science':
        s = input('Choose your course = ')
        match s:
            case 'Medical':
                print('Choose path : Science -> Medical')
            case 'Engineering':
                print('Choose path : Science -> Engineering')
            case _:
                print('Invalid Subject')
    case 'Commerce':
        s = input('Choose your course = ')
        match s:
            case 'CA':
                print('Choose path : Commerce -> CA')
            case 'B.com':
                print('Choose path : Commerce -> B.com')
            case _:
                print('Invalid Subject')
    case ' Arts':
        s = input('Choose your course = ')
        match s:
            case 'History':
                print('Choose path :  Arts -> History')
            case 'Literature':
                print('Choose path :  Arts -> Literature')
            case _:
                print('Invalid Subject')



# #8 question

show = int(input('Enter a timing = '))
if show >= 9 and show <= 12:
    print('Morning Show')
elif show > 12 and show <=16:
    print('Matinee Show')
elif show > 16 and show <= 20:
    print('Evening Show')
elif show > 20 and show <=24:
    print('Night Show')
else:
    print('Invalid Timing')

# 9 question
d = float(input("Enter the distance in km"))
choice = input("Enter the Conversion")
match choice:
    case "meter":
        print(d*1000,"m")
    case "centimeter":
        print(d*100000,"cm")
    case "millimeter":
        print(d*1000000,"mm")
    case "miles":
        print(d*0.621371,"miles")
    case _ :
        print("Invalid Conversion")

# 10 question


pm = (input("Enter the input"))
if pm == "UPI":
    print("You selected UPI payment")
elif pm == "Card":
    print( "You selected Debit/Credit Card payment")
elif pm == "Net Banking":
    print("You selected Net Banking")
elif pm == "COD":
    print("You selected Cash on Delivery")
else:
    print("Invalid Payment Mode")
