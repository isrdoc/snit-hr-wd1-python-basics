import random

SECRET = random.randint(1, 30)
attempts = 10

while True:
    print("Attempts left: " + str(attempts))
    attempts -= 1
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if attempts == 0:
        print("Out of attempts")
        break

    if guess == SECRET:
        print("You've guessed it - congratulations! It's number 22.")
        break

    print("Sorry, your guess is not correct... The secret number is not " + str(guess))

    if guess > SECRET:
        print("Try something smaller")
        continue

    print("Try something bigger")

print("End")
