# water_level = 50
# if water_level >80:
#   print("Drain water")
# else:
#   print("Continue")

# Practice 1
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride the rollercoaster!")
# else:
#   print("Sorry, you have to grow taller before you can ride.")


# Challenge 1
# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if number%2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


# # Practice 2
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age <= 18:
#     print("Please pay $7.")
#   else:
#     print("Please pay $12")
# else:
#   print("Sorry, you have to grow taller before you can ride.")


# # Practice 3
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     print("Please pay $5.")
#   elif 12 <= 18:
#     print("Please pay $7.")
#   else:
#     print("Please pay $12")
# else:
#   print("Sorry, you have to grow taller before you can ride.")


# # challenge 2
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = weight / (height ** 2)
# bmi_r = round(bmi, 0 )
# bmi_i = int(bmi_r)
# if bmi_i < 18.5:
#     print(f"Your BMI is {bmi_i}, you are underweight.")
# elif bmi_i < 25:
#     print(f"Your BMI is {bmi_i}, you have a normal weight.")
# elif bmi_i < 30:
#     print(f"Your BMI is {bmi_i}, you are slightly overweight.")
# elif bmi_i < 35:
#     print(f"Your BMI is {bmi_i}, you are obese.")
# else:
#     print(f"Your BMI is {bmi_i}, you are clinically obese.")

# #Challenge 3
# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# Practice 4
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   else:
#     bill = 12
#     print("Adult tickets are $12")
  
#   wants_photo = input("Do you want a photo taken?  Y or N. ")
#   if wants_photo == "Y":
#     bill += 3
    
#   print(f"Your final bill is ${bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# Practice 4
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age >= 45 and age <= 55:
    bill = 0
    print("Everythin is goingto be ok. Have a free ride on us!")
  elif age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12")
  
  wants_photo = input("Do you want a photo taken?  Y or N. ")
  if wants_photo == "Y":
    bill += 3
    
  print(f"Your final bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride.")
  
# Challenge 4
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
testname = name1.lower() + " " + name2.lower()

tc = int(testname.count("t"))
rc = int(testname.count("r"))
uc = int(testname.count("u"))
ec = int(testname.count("e"))

lc = int(testname.count("l"))
oc = int(testname.count("o"))
vc = int(testname.count("v"))
ec = int(testname.count("e"))

score_true = str(tc + rc + uc + ec)
score_love = str(lc + oc + vc + ec)
lovescore = int(score_true + score_love)

if lovescore > 90 or lovescore < 10:
  print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore >= 40 and lovescore <= 50:
  print(f"Your score is {lovescore}, you are alright together.")
else:
  print(f"Your score is {lovescore}.")
