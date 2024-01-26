from utils import select_bot
from game import Game

def main():
    bot = select_bot()
    game = Game(bot)
    if game.test():
        print('All tests passed!')
    else:
        print('Tests failed!')

if __name__ == '__main__':
    main()