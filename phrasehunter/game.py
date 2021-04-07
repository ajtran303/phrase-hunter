import random

from .phrase import Phrase

class Game():

    phrases = [
        Phrase('Hello World'),
        Phrase('Hello Mother'),
        Phrase('Hello Father'),
        Phrase('Here I am at'),
        Phrase('Camp Granada'),
    ]

    def __init__(self):
        self.phrases = Game.phrases
        self.missed = 0
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.active_phrase = self.get_random_phrase()
        print(self.welcome())
        self.play_game()
        print('\n', self.game_over(self.is_winner()), '\n')
        print('The phrase was:', self.active_phrase.phrase.upper())
        self.ask_to_play_again()

    def is_loser(self):
        return self.missed == 5

    def is_winner(self):
        return self.active_phrase.check_complete()

    def play_game(self):
        while True:
            if self.is_loser() or self.is_winner():
                break
            print(self.active_phrase.display(), '\n')
            self.handle_guess()
            print(f'{5 - self.missed} misses remaining!')

    def handle_guess(self):
        try:
            result = self.active_phrase.check_letter(self.get_guess())
            if result is False:
                self.missed += 1
        except ValueError as err:
            print(err)

    def welcome(self):
        return 'Welcome to the Phrase Hunting game!\n'+\
               '- Win by guessing all the letters!\n'+\
               '- Lose by missing five (5) guesses!\n'+\
               '- Quit with `<control>+C` or `<control>+D`\n'

    def game_over(self, win):
        return {
            False: 'Game over! You lose!',
            True: 'You won! Game over!'
        }[win]

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def get_guess(self):
        guess = input('Guess a letter:  ').lower()
        if len(guess) > 1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
            raise ValueError('Please pick one letter.')
        elif guess in self.guesses:
            raise ValueError(f'You already guessed `{guess}`')
        else:
            self.guesses.append(guess)
        return guess

    def ask_to_play_again(self):
        answer = input('\nSend Y to play again or any other key to quit:  ')
        if answer.lower() == 'y':
            self.active_phrase.reset()
            print('\n')
            new_game = Game()
            new_game.start()
        else:
            print('\nGoodbye and thank you for playing!')
