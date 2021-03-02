import random
import json
import datetime
from greetings import print_greeting

secret = random.randint(1, 30)
attempts = 0

print_greeting("Hello", "player")

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    top_scores_message = "Top scores: "
    number_of_top_scores = 3
    top_three_scores = score_list[:number_of_top_scores]

    for index, score in enumerate(top_three_scores):
        top_scores_message += str(score["attempts"])
        if index + 1 < number_of_top_scores:
            top_scores_message += ", "
    print(top_scores_message)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        current_time = datetime.datetime.now()
        score_list.append({
            "attempts": attempts,
            "date": str(current_time)
        })
        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
