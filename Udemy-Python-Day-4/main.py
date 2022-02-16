import random
# import my_module
# print(my_module.pi)

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_float * 5

love_score = random.randint(1, 100)
print(f"Your love socre is {love_score}")

# Challenge 1
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
test = random.randint(0 , 1)
if test == 0:
  print("Tails")
else:
  print("Heads")
