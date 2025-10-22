# task no 1
# 1. Write a function to split a given string on hyphens (-) and display each substring on a new line.
# You must:
# - Solve it using an inbuilt function (split()).
# - Solve it without using any inbuilt split functions — by using loops and conditions.
# Given:
# sentence = "Emma-is-a-data-scientist"
# Expected Output:
# Emma
# is
# a
# data
# scientist


def sentence(s):
    new = s.split("-")
    for i in new:
        print(i)
sentence("Emma-is-a-data-scientist")

# task 2

# 2. Write a Python program to reverse a given string in two ways:
# - Using an inbuilt function or slicing
# - Without using any inbuilt functions/Slicing
# Given:
# str1 = "Python"
# Expected Output:
# nohtyP


def reverse (s):
    foo=""
    for i in s:
        foo=i+foo
    print(foo)
reverse("Python")

# task 3

# 3. Write a Python program to count the number of consonants in a given string.
# Input:
# Hello World
# Output:
# Number of consonants: 7

def find_consonant(s):
    count=0
    for i in s:
        if i!="a" and i!="e" and i!="i" and i!="o" and i!="u" and i!=" ":
            count=count+1
    print(count)
  
find_consonant("Hello World")

# task 4

# 4.  Write a Python program to remove all spaces from a given string.
# Input:
# Python is awesome
# Output:
# Pythonisawesome

def remove_all_spaces(s):
    count=""
    for i in s:
        if i!=" ":
            count=count+i
    print(count)

remove_all_spaces("Python is awesome")

# task 5

# 5. Write a Python program that asks the user to enter a password and checks if it is strong. A password is considered strong if:
# It has at least 8 characters and  atleast one special character (!@#$%^&*).
# Print whether the password is strong or not.
# Input:
# Password: my@password
# Output:
# Password is strong
# Input:
# Password: python123
# Output:
# Password is not strong

def passwords(n):
    special_characters = "!@#$%^&*"
    if len(n) < 8:
        print("Password is not strong")
    else:
        for char in n:
            if char in special_characters:
                print("Password is strong")
                break
        else:
            print("Password is not strong")

        
passwords("my@password")
passwords("python123")


