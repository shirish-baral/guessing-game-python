import random
import logo_art
# Declare global variables and set constant
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTTEMPTS=5

# Function to check level
def set_difficulty(level):
    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level == 'hard':
        return HARD_LEVEL_ATTTEMPTS
    else:
        print("Enter valid input")

#Function to check guessed number
def check_number(guess,number,attempts):
    if guess < answer:
        print("Your guess is lower ")
        return attempts-1
    elif guess > answer:
        print("Your guess is higher")
        return attempts-1
    else:
        print(f"Your guess is correct. Answer is {answer}")

# Print 'Guess Number' art from logo-art.py        
print(logo_art.logo)        

#Take input from user
print("Welcome to Game!!")
low = int(input("Enter lower range: "))
high = int(input("Enter higher range: "))

print(f"Let me think of a number between {low} to {high}.")
answer = random.randint(low,high)
print(answer)
level = input("Enter challenging level: (easy or hard): ")
attempts = set_difficulty(level)

# Take input again
guess = 0
while guess != answer:
    print(f"You have {attempts} remanining")
    guess = int(input("Guess the number: "))
    attempts=check_number(guess,answer,attempts)
    if attempts==0:
        print("You lose! No more attempts remaining!")
        break
    elif answer!= guess:
        print("Guess again")

    
    






