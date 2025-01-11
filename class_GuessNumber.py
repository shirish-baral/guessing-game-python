# This code was created with the assistance of OpenAI's ChatGPT for educational purposes.

import random
import logo_art

# Declare constants for attempts
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

class NumberGuessingGame:
    def __init__(self, low, high, level):
        """Initialize the game with range, difficulty level, and attempts."""
        self.low = low
        self.high = high
        self.answer = random.randint(low, high)
        self.attempts = self.set_difficulty(level)
        self.guess = None

    def set_difficulty(self, level):
        """Set the number of attempts based on difficulty."""
        if level == 'easy':
            return EASY_LEVEL_ATTEMPTS
        elif level == 'hard':
            return HARD_LEVEL_ATTEMPTS
        else:
            print("Invalid level! Defaulting to 'easy'.")
            return EASY_LEVEL_ATTEMPTS

    def check_guess(self, guess):
        """Check the guessed number and provide feedback."""
        if guess < self.answer:
            print("Your guess is lower.")
            return False
        elif guess > self.answer:
            print("Your guess is higher.")
            return False
        else:
            print(f"Congratulations! You guessed the correct number: {self.answer}.")
            return True

    def play(self):
        """Run the game loop."""
        print(f"Let me think of a number between {self.low} and {self.high}.")
        # Debugging: Uncomment to see the answer
        # print(f"Answer (for debugging): {self.answer}")

        while self.attempts > 0:
            print(f"You have {self.attempts} attempts remaining.")

            # Validate that the input is a number within the range
            while True:
                user_input = input("Guess the number: ")
                if user_input.isdigit():
                    self.guess = int(user_input)
                    if self.low <= self.guess <= self.high:
                        break
                    else:
                        print(f"Please enter a number between {self.low} and {self.high}.")
                else:
                    print("Invalid input! Please enter a valid number.")

            # Check the guess
            if self.check_guess(self.guess):
                break

            # Decrease attempts and check if the user has lost
            self.attempts -= 1
            if self.attempts == 0:
                print(f"Game Over! You've run out of attempts. The correct number was {self.answer}.")
            else:
                print("Guess again!")

# Main game logic
if __name__ == "__main__":
    print(logo_art.logo)  # Print ASCII art logo
    print("Welcome to the Number Guessing Game!")

    # Validate range inputs
    while True:
        low_input = input("Enter lower range: ")
        high_input = input("Enter higher range: ")
        if low_input.isdigit() and high_input.isdigit():
            low = int(low_input)
            high = int(high_input)
            if low < high:
                break
            else:
                print("The lower range must be less than the higher range.")
        else:
            print("Invalid input! Please enter valid numbers.")

    # Validate difficulty level
    while True:
        level = input("Enter difficulty level (easy or hard): ").lower()
        if level in ['easy', 'hard']:
            break
        else:
            print("Invalid level! Please choose 'easy' or 'hard'.")

    # Create a game instance and start the game
    game = NumberGuessingGame(low, high, level)
    game.play()
 