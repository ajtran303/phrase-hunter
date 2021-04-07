import random

class Game():

    def __init__(self, *phrases):
        self.phrases = list(phrases)
        self.missed = 0
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.active_phrase = self.get_random_phrase()
        print(self.welcome())
        self.play_game()
        print('\n', self.game_over(win=self.is_winner()), '\n')
        print('The phrase was:', self.active_phrase.phrase.upper())

    def is_loser(self):
        return self.missed == 5

    def is_winner(self):
        return self.active_phrase.check_complete()

    def play_game(self):
        while True:
            if self.is_loser() or self.is_winner():
                break

            print(self.active_phrase.display(), '\n')
            guess = self.get_guess()
            result = self.active_phrase.check_letter(guess)
            if result is False:
                self.missed += 1
            print(f'{5 - self.missed} misses remaining!')

    def welcome(self):
        return 'Welcome to the phrase hunting game!'

    def game_over(self, win=False):
        # ends the game too?
        return {
            False: 'Game over! You lose!',
            True: 'You won! Game over!'
        }[win]

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def get_guess(self):
        guess = input('Guess a letter:  ').lower() # needs validation
        self.guesses.append(guess)
        return guess
