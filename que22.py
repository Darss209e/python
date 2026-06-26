import random

random_number = random.randint(1, 100)
num = int(input("Guess a number between 1 and 100: "))  
if num==random_number:
    print("Congratulations! You guessed the correct number.")   
else:
    print("Sorry, that's not the correct number.")  ``