from bots.bot import Bot
class ChumpBot(Bot):
    def __init__(self):
        super().__init__()
    
    def load_guesses(self):
        pass

    def guess(self, game_state):
        return 'chump'