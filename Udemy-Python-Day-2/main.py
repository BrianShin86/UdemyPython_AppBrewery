#Data Types

#Strings

# print("Hello"[4])

# print("123" + "345")

#Integer

# print(123+345)

# 123_456_789

# Float

# 3.14159

# Boolean

# True
# False

# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# a= float(123)
# print(type(a))

# print(70 + float("100.5"))
# print(str(70) + str(100))

# Challenge 1
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
A = two_digit_number [0]
B = two_digit_number [1]
print (int(A) + int(B))

3 + 5
7 - 4
3 * 2
# print(type(6/2))
6 / 3
# print(2 ** 3) power function

# PEMDASLR
# Parentheses ()
# Multiplication **
# *
# Division /
# Addition +
# Subtraction -

# print(int(3*3+3/3-3))
# print(3*(3+3)/3-3)

# a = 80/(1.75*1.75)

# print(int(a))

# Challenge 2 BMI calculator

height = input("Height in m?\n")
weight = input("Weight in kg?\n")
h = float(height)
w = str(weight)
bmi = h/(w ** 2)
print(str(bmi))

#print(round(8/3))
#print(round(8/3,2))
#print(round(2.66666,2))
#print(8//3)

score = 0
height = 1.8
isWinning = True

#f-String
print(f"Your score is {score}, your height is {height}, you are winning {isWinning}")

# Challenge 3

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
end_day = 90 * 365
end_week = 90 * 52
end_year = 90 * 12
current_day = int(age)*365
current_week = int(age)*52
current_year = int(age)*12
r_day = int(end_day) - int(current_day)
r_week = int(end_week) - int(current_week)
r_year = int(end_year) - int(current_year)
print(f"You have {r_day} days, {r_week} weeks, and {r_year} months left.")
