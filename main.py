#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please guess a letter: ")
guess = guess.lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
length = len(guess)
for letters in chosen_word:
  if length != 0:
    if chosen_word[length] == guess:
      print(guess)
      length -= 1
    else:
      print("You lose")