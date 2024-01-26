from utils import *
from game import Game


def train():
    # Trains a bot of your choice
    bot = select_bot()
    game = Game(bot, train=True)
    game.train()
    save(bot, f'bots/saved/{bot.__class__.__name__}.pkl')

if __name__ == '__main__':
    train()