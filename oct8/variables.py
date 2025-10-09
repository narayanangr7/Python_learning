password = input("Enter your password :")
print("Your password has been successfully uploaded.")
while True:
    s = input("Enter password: ")
    if s == password:
        print("Access granted")
        break
    else:
        print("Wrong password, try again!")
