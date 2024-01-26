import pickle
from bots.chump_bot import ChumpBot

def select_bot():
    bots = [ChumpBot]

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

def save(bot, name):
    # Pickle this object to bots/saved/chump_bot.pkl
    pickle.dump(bot, open(f'bots/saved/{name}.pkl', 'wb'))

def load(name):
    # Load the pickled object from bots/saved/chump_bot.pkl
    return pickle.load(open(f'bots/saved/{name}.pkl', 'rb'))