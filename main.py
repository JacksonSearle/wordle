from game import Game
from bots.chump_bot import ChumpBot

def manually_use_bot():
    bots = [ChumpBot]

    # Print out each class name
    print('Select a bot:')
    for i, bot in enumerate(bots):
        print(f'{i}: {bot.__name__}')

    # Get user input
    selection = input()
    bot = bots[int(selection)]()

    # Play the game
    game = Game(bot)
    game.manually_use_bot()


if __name__ == '__main__':
    manually_use_bot()