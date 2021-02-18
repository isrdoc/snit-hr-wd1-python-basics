secret = 22
guess = 0
number_of_attempts = 3

has_user_guessed = False
is_number_of_attempts_reached = False

while (not has_user_guessed) and (not is_number_of_attempts_reached):
    print("Attempts left: " + str(number_of_attempts))
    number_of_attempts = number_of_attempts - 1
    is_number_of_attempts_reached = number_of_attempts == 0

    guess = int(input("Guess the secret number (between 1 and 30): "))
    has_user_guessed = guess == secret

    if guess == secret:
        print("You guessed it - congratulations! It's number 22.")
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))

print("Done")
