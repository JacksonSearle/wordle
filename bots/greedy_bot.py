from bots.bot import Bot


class GreedyBot(Bot):
    def __init__(self):
        self.load_guesses()
    
    def load_guesses(self):
        pass

    def guess(self, game_state):
        return 'chimp'
    
    def record(self, game_state):
        pass
