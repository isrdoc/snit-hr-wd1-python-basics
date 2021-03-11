import datetime
from file_utils import read_json_from_file, write_json_to_file
from guess_game import SecretNumberGame

new_game = SecretNumberGame()

attempts = 0
scores_file = "score_list.json"

score_list = read_json_from_file(scores_file)

print(f"Top scores: {score_list}")

for score_dict in score_list:
    _attempts = score_dict['attempts']
    _date = score_dict.get('date')
    print(f"{_attempts} attempts, date: {_date}")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    game.do_guess(guess)
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
        write_json_to_file(score_list, scores_file)

        print(f"You've guessed it - congratulations! It's number {secret}")
        print(f"Attempts needed: {attempts}")
        break

    print(game.suggest_on_missed())
