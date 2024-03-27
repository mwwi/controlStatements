import random  # Importing the random module for generating random numbers

while True:
    # Generate a random number between 1 and 10 for each game
    hidden_number = random.randint(1, 10)

    # Iterate through 3 chances
    for _ in range(3):
        # Get user's guess
        guess = int(input("Guess the number between 1 and 10: "))

        # Check if guess is correct
        if guess == hidden_number:
            print("Congratulations! You guessed the number correctly.")
            break
        elif guess < hidden_number:
            print("Try again. The hidden number is higher.")
        else:
            print("Try again. The hidden number is lower.")
    else:
        # If the loop completes without a correct guess
        print("Sorry, you've run out of chances. The hidden number was:", hidden_number)

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break
