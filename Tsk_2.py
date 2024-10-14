# # Problem 1
# # Write a Python program that prompts the user for a number and determines whether the number is even or odd.

# num = int(input("Write any number "))
# def even_odd(number):
#     if number % 2 == 0:
#       return "even"
#     else :
#        return "odd"
# result = even_odd(num)    
# print("The given number is " + result)

# Problem 2
# Create a Python program that generates the Fibonacci sequence up to a specified number n.
# num = int(input("Write any any integer number "))
# def Fibonacci(n):
#     series=[]
#     while n>=0:
#       n = (n-1) + (n-2)
#       print(n)
#       return series
# res = Fibonacci(num)

# Problem 3
# Write a Python function to check whether a given string is a palindrome.


# def isPalindrome(s):
#     return n == n[::-1]

# n = input("Enter any number or word ")
# ans = isPalindrome(n)

# if ans:
#     print("Yes")
# else:
#     print("No")


# Problem 4
# Write a Python program that calculates the sum of all natural numbers from 1 to n, where n is given by the user
# num = int(input("Write any integer number"))
# sum = 0
# for i in range (1 , num+1):
#   sum += i 
# print(sum)

# Problem 5
# Write a Python program to find the largest number among three given numbers.
# num1=input("Write any number ")
# num2=input("Write any number ")
# num3=input("Write any number ")
# Largest_num = []
# if (num1>num2):
#     Largest_num = num1
# elif(num2>num3):
#     Largest_num = num2
# elif(num3>num1):
#     Largest_num = num3
# print(Largest_num)

# Problem 6
# Create a Python function that calculates the factorial of a given number n.
# num = int(input("Write any integer number "))
# fact = 1
# for i in range (1 , num+1):
#   fact = fact*i 
# print(fact)

# Problem 7
# Write a Python program that checks if a given number is a prime number.

# num = int (input ("Enter any number: "))
# prime = False
# if num > 1:
#   for i in range (2, num):
#     if (num % i) == 0:
#       prime = True
# if prime:
#   print ("The number entered is not a prime number")

# else:
#   print ("The number entered is a prime number")

# Problem 8
# Write a Python function that reverses a string provided by the user.

# word = input("Enter any number or word ")
# def reverse(word):
#     return word[::-1]

# ans = reverse(word)
# print(ans)

# Problem 9
# Create a Python program that counts the number of vowels in a given string.
# word = input("Enter any word or sentence: ")
# def count_vowels(c):
#   count = 0
#   vowels = "aeiouAEIOU"
#   for char in c:
#         if char in vowels:
#           count+=1
#   return count
# result = count_vowels(word)
# print(result)

# Problem 10
# Implement a Python program where the computer randomly selects a number between 1 and 100, and the user tries to guess the number. Provide feedback to the user whether their guess is too high, too low, or correct.
# import numpy as np
# number = np.random.randint(1, 101)
# while True:
#    guess = int(input("Guess any number "))
#    if guess < number:
#             print("Your guess is too low. Try again.")
#    elif guess > number:
#             print("Your guess is too high. Try again.")
#    else:
#            print("Congratulations! You've guessed the correct number")
#            break 
# print(number)

# Problem 11
# Write a Python program to implement a simple calculator that performs addition,subtraction, multiplication, and division.
# num1 = int(input("Write first number "))
# num2 = int(input("Write second number "))
# perform = input("Write function you wanna perform ")
# if perform =="+":
#        num = num1+num2
#        print("The sum of two numbers is: " + str(num))
# elif perform =="-":
#        num = num1-num2
#        print("The subtraction of two numbers is: " + str(num))
# elif perform=="*":
#        num = num1*num2
#        print("The multiplication of two numbers is: " + str(num))
# elif perform =="/":
#        num = num1/num2
#        print("The division of two numbers is: " + str(num))
# else:
#        print("not exist")

# Problem 12
# Write a Python program that calculates the sum of the digits of a given number.
# num1 = int(input("Write first number "))
# num2 = int(input("Write second number "))
# num = num1+num2
# print("The sum of two numbers is: " + str(num))

# Problem 13
# Write a Python program to check if a given year is a leap year.
# year = int(input("Enter a year "))
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("Given year is a leap year")
#     else:
#         print("Given year is not a leap year")
        
# is_leap_year(year)

# Problem 14
# Write a Python function to check if a given number is an Armstrong number.
number = int(input("Enter a number: "))
def is_armstrong(num):
   return num == sum(int(digit) ** len(str(num)) for digit in str(num))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


# Problem 15
# Write a Python program that prints the multiplication table for a given number n.
# num = int(input("Write any number: "))
# n = int(input("Enter num wher you want to stop table "))
# def multiply(number):
#   for i in range(1,n+1):
#     result = number * i 
#     print(f"{number} x {i} = {result}")
# multiply(num)