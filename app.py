from phrasehunter.game import Game

if __name__ == '__main__':
    try:
        game = Game()
        game.start()
    except EOFError:
        print('\n\nGoodbye!')
        quit()
    except KeyboardInterrupt:
        print('\n\nGoodbye!')
        quit()
