from utils import select_bot
from game import Game

def main():
    bot = select_bot()
    print(f'\nTesting {bot.__class__.__name__}...')
    game = Game(bot)
    if game.test():
        print('All tests passed!')
    else:
        print('Tests failed!')

if __name__ == '__main__':
    main()