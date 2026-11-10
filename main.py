import random

## Program Start 
start_message = """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances) 
"""
print(start_message)

chosen_diff = False

## The difficulity level 
while chosen_diff == False:
    try: 
        diff_level: int = int(input("Enter the number of your desired difficulity: "))
        if diff_level == 1: 
            print("I guess a casual game is always fun.")
            chosen_diff = True
        elif diff_level == 2: 
            print("Perfect. A slight challange is always fun.")
            chosen_diff = True
        elif diff_level == 3: 
            print("Big boy alert. Good luck.")
            chosen_diff = True
        else:
            print("Enter a valid number (1, 2, or 3).")
            chosen_diff = False
    except ValueError:
        print("Write the difficulty level according to the list, not by name.")
        chosen_diff = False 

## Generating the random number 
if chosen_diff == True:
    random_number: int = random.randint(1, 100)

## Prompting the user to guess the number
user_guess: int = int(input("Make your guess: "))

## Core game logic
try: 
    if user_guess == random_number:
        print("Congrats!!! You guess the number!")
        user_guess = int(input("Enter Your new number: "))
    elif user_guess > random_number:
        print(f"The number is less than {user_guess}")
        user_guess = int(input("Enter Your new number: "))
    elif user_guess < random_number:
        print(f"The number is bigger than {user_guess}")
        user_guess = int(input("Enter Your new number: "))
except Exception as e:
    print(f"Something is wrong: {e}")


