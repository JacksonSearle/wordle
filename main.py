from utils import *
from game import Game


def manually_use_bot():
    # Play the game
    game = Game(select_bot())
    game.manually_use_bot()

if __name__ == '__main__':
    manually_use_bot()