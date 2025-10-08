sum=0
for i in range(1,6):
    sum=sum+i
print(sum)

#====================================================================

n=int(input("enter your number"))
for i in range (1,10+1):
    print(i*n)

#=======================================================================

n=int(input("enter your number"))
sum=1
for i in range (n,1,-1):
    sum=sum*i
    
print(sum)

#=======================================================================
word="red"
word_len = len(word)
mid = word_len/2
if word_len%2==1:
    for i in range(word_len):
        distence = int(i - mid)
        print(word[i]*distence)


#===========================================================================\

total = 0
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    total += n
print("Total sum:", total)


i = 1
while i <= 50:
    if i % 3 == 0:
        print(i)
    i += 1


n = int(input("Enter a number to start countdown: "))
while n >= 1:
    print(n)
    n -= 1
print("Time's up!")


password = input("Enter your password :")
print("Your password has been successfully uploaded.")
while True:
    s = input("Enter password: ")
    if s == password:
        print("Access granted")
        break
    else:
        print("Wrong password, try again!")
