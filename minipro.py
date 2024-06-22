import random

def number_guessing_game():
    # Get the range from the user
    x = int(input("Enter the lower bound of the range: "))
    y = int(input("Enter the upper bound of the range: "))

    # Generate a random number in the range
    secret_number = random.randint(x, y)

    # Initialize the number of guesses
    num_guesses = 0

    # Initialize the range
    lower_bound = x
    upper_bound = y

    # Play the game
    while True:
        # Ask the user for their guess
        guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))

        # Check if the guess is correct
        if guess == secret_number:
            print(f" Congratulations! You guessed the number in {num_guesses + 1} guesses.")
            break

        # Update the range based on the guess
        if guess < secret_number:
            lower_bound = guess + 1
        else:
            upper_bound = guess - 1

        # Increment the number of guesses
        num_guesses += 1

if __name__ == "__main__":
    number_guessing_game()