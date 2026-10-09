import random

play_again = "y"

while play_again == "y":
    number = random.randrange(1, 1001)
    guess = 0

    print("Guess my number between 1 and 1000 with the fewest guesses:")

    while guess != number:
        guess = int(input("Your guess: "))

        if guess > number:
            print("Too high. Try again.")
        elif guess < number:
            print("Too low. Try again.")

    print("Congratulations. You guessed the number!")

    play_again = input("Play again? (y/n): ").lower()
