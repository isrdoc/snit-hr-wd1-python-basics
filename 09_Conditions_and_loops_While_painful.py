secret = 22
attempts = 3

while True:
    print("Attempts left: " + str(attempts))
    attempts -= 1
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if attempts <= 0:
        print("Out of attempts, WHY???")
        continue

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
        break

    print("Sorry, your guess is not correct... The secret number is not " + str(guess))
    print("End of iteration")

print("End of loop")
