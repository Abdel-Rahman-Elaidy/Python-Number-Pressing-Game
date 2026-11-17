import random

# Functions

# The if-logic (as refrenced in task 4 document)
def game_logic(guess, target):
    try: 
        if guess == target:
            print(f"Congrats!! You guessed the number in {chances} trails")
            return True
        elif guess > target:
            print(f"The number is less than {guess}")
            return False
        elif guess < target:
            print(f"The number is bigger than {guess}")
            return False
    except Exception as e:
        print(f"Something is wrong: {e}")

# Program Start 
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
chances = 0

# The difficulity level 
while chosen_diff == False:
    try: 
        diff_level: int = int(input("Enter the number of your desired difficulity: "))
        if diff_level == 1: 
            print("I guess a casual game is always fun.")
            chosen_diff = True
            chances = 10
        elif diff_level == 2: 
            print("Perfect. A slight challange is always fun.")
            chosen_diff = True
            chances = 5
        elif diff_level == 3: 
            print("Big boy alert. Good luck.")
            chosen_diff = True
            chances = 3
        else:
            print("Enter a valid number (1, 2, or 3).")
            chosen_diff = False
    except ValueError:
        print("Write the difficulty level according to the list, not by name.")
        chosen_diff = False 

# Generating the random number 
if chosen_diff == True:
    random_number: int = random.randint(1, 100)

for chances in range(1, chances + 1):
    user_guess: int = int(input("Make your guess: "))
    if game_logic(user_guess, random_number) == True:
        break
    if diff_level == 1 and chances == 10:
        print("Oh no. You have finished all your chances.")
    elif diff_level == 2 and chances == 5:
        print("Oh no. You have finished all your chances.")
    elif diff_level == 3 and chances == 3:  
        print("Oh no. You have finished all your chances.")
    
   


