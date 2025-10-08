# Python: Debugging

def sum_numbers(n):
    sum = 0
    i = 0
    while i <= n:
        sum += i
        i += 1
    return sum
n = 5
result = sum_numbers(n)
print(f"The first {n} terms of the series are: {result}")

#=============================================================================

def calculate_grade(score):
    if score > 100 or score < 0:
        print("Invalid valew")
    else:
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        elif score >= 70:
            print("Grade: C")
        elif score >= 60:
            print("Grade: D")
        else:
            print("Grade: F")

score = 5
result = calculate_grade(score)

#========================================================================
n=int(input("Enter your number"))
a=0
b=1
i=0
while a<=n:
    print(a)
    temp=a+b
    a=b
    b=temp
    i+=1

#============================================================================

j = int(input("Enter the n value = "))
s = 0
n = j
while j > 0:
    r = j % 10
    s = s + r * r * r
    j = j // 10   # integer division
if n == s:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")

h=int(input("emter your number"))
w=int(input("enter your white"))
formila=w//h**2
print(formila)
if formila<=18:
    print("under wight")
elif formila>=18 and formila<=25:
    print("normel wight")
elif formila>=25:
    print("obese")

height=float(input("Enter your height:"))
weight=float(input("enter your weight:"))
BMI=weight/(height**2)
print(BMI)
if BMI<18:
    print("under_weight")
elif BMI>18 and BMI<25:
    print("normal")
elif BMI>25 and BMI<29:
    print("overweight")
elif BMI>=30:
    print("Obese")

n = int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0:
        print(n, "is not a prime number")
        break
else:
    print(n, "is a prime number")


