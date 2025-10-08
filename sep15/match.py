rating = int(input("Enter your number"))

match rating:
    case 1:
        print("very bad")
    case 3:
        print("average")
    case 4:
        print("good")
    case 5:
        print("excelient")
    case 2:
        print("bad")

    case _:
        print("Invalid rating")
# ==================================================
def find_grade(mark):
    #Write your code here
    if mark>=75:
     print("You got an A grade")
    elif mark>=60 and mark<75:
     print("You got a B grade")
    elif mark>=45 and mark<60:
     print("You got a C grade")
    elif mark<45:
     print( "You didn't get an A, B or C grade")
find_grade(83)
# ============================================
