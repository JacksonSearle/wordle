from utils import *
from game import Game


def train():
    # Trains a bot of your choice
    bot = select_bot()
    game = Game(bot)
    game.train()
    bot.save()



if __name__ == '__main__':
    train()