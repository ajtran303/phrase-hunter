from phrasehunter.game import Game
from phrasehunter.phrase import Phrase

if __name__ == '__main__':
    phrase_1 = Phrase('Hello World')
    phrase_2 = Phrase('Hello Mother')
    phrase_3 = Phrase('Hello Father')
    phrase_4 = Phrase('Here I am at')
    phrase_5 = Phrase('Camp Granada')
    phrase_6 = Phrase('World Hello')
    phrase_7 = Phrase('Mother Hello')
    phrase_8 = Phrase('Father Hello')
    phrase_9 = Phrase('I am here at')
    phrase_10 = Phrase('Granada Camp')
    phrases = (phrase_1, phrase_2, phrase_3, phrase_4, phrase_5,
               phrase_6, phrase_7, phrase_8, phrase_9, phrase_10)

    game = Game(*phrases)
    game.start()
