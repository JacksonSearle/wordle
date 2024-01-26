import pickle
from bots.chump_bot import ChumpBot
from bots.greedy_bot import GreedyBot

def select_bot():
    bots = [ChumpBot, GreedyBot]

    # Print out each class name
    print('Select a bot:')
    for i, bot in enumerate(bots):
        print(f'{i}: {bot.__name__}')

    # Get user input
    while True:
        selection = input()
        if selection.isdigit() and int(selection) in range(len(bots)):
            break
        else:
            print('Invalid selection. Please try again.')

    bot = bots[int(selection)]()
    
    return bot

def save(object, path):
    # Pickle this object
    pickle.dump(object, open(path, 'wb'))

def load(path):
    # Load the pickled object
    return pickle.load(open(path, 'rb'))