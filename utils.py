from bots.chump_bot import ChumpBot

def select_bot():
    bots = [ChumpBot]

    # Print out each class name
    print('Select a bot:')
    for i, bot in enumerate(bots):
        print(f'{i}: {bot.__name__}')

    # Get user input
    selection = input()
    bot = bots[int(selection)]()
    
    return bot