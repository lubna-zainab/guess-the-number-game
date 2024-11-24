import random

def guess_the_number_game():
    print("Welcome to the Guess the Number Game!")
    print("""
    Type 'Start' to start the game
    Type 'Help' for instructions on How to Play
    Type 'Quit' to quit the game
    """)
    
    while True:
        user_input = input("Enter the command (Start/Help/Quit): ").lower()
        
        if user_input == "quit":
            print("You have quit the game.")
            break
        elif user_input == "help":
            print("""
            Instructions:
            1. You will guess a number chosen by the computer.
            2. You will select a difficulty level: Easy, Medium, or Hard.
            3. Based on the difficulty, you will have a specific number of attempts and a required range difference.
            4. Guess the number within the allowed attempts.
            5. The game will give you hints if your guess is 'Too high' or 'Too low' than the number chosen by the computer.
            6. You can type 'quit' anytime to exit the game.
            """)
        elif user_input == "start":
            print("Starting the game...")
            start_game()
        else:
            print("Invalid command. Please type 'start', 'help', or 'quit'.")

def start_game():
    while True:
        difficulty = input("Select difficulty (Easy/Medium/Hard): ").lower()
        
        if difficulty == "easy":
            min_range = 10
            attempts = 5
            break
        elif difficulty == "medium":
            min_range = 20
            attempts = 4
            break
        elif difficulty == "hard":
            min_range = 30
            attempts = 3
            break
        else:
            print("Invalid difficulty. Please choose Easy, Medium, or Hard.")


    while True:
        try:
            print("Please set the upper and lower limit of the number range.")
            lower_limit = int(input("Enter the lower limit: "))
            upper_limit = int(input("Enter the upper limit: "))
            
            if lower_limit >= upper_limit:
                print("Lower limit must be lesser than upper limit. Please try again.")
            elif upper_limit - lower_limit < min_range:
                print(f"The range is too narrow. It must be at least {min_range}. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter integers.")


    secret_number = random.randint(lower_limit, upper_limit)

    print(f"I have selected a number between {lower_limit} and {upper_limit}. Can you guess it?")
    print(f"You have {attempts} attempts. Type 'quit' to exit anytime.")
    

    while attempts > 0:
        guess_input = input(f"\nYou have {attempts} attempts left. Enter your guess: ").lower()

        if guess_input == "quit":
            print("You have quit the game.")
            return
        
        try:
            guess = int(guess_input)
            attempts -= 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly! YOU WIN! :)")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"\nYou've run out of attempts! The correct number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    guess_the_number_game()