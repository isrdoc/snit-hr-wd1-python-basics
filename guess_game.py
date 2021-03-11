import random


class SecretNumberGame:
    def __init__(self, secret):
        self.secret = random.randint(1, 30)
        if secret:
            self.secret = secret
        self.guess = None

    def do_guess(self, guess):
        self.guess = guess

    def suggest_on_missed(self):
        _guess_incorrect = "Your guess is not correct..."
        _try_string = "Try something"
        if self.guess > self.secret:
            return f"{_guess_incorrect} {_try_string} smaller"
        elif self.guess < self.secret:
            return f"{_guess_incorrect} {_try_string} bigger"
