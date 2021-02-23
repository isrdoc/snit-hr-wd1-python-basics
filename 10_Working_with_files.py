import random

secret = random.randint(1, 10)
attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
print(f"Best score {best_score}")

while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
            print("Congratulations! You've made the best score!")
            break
        print("Nice try. Try again to beat the best score.")
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
