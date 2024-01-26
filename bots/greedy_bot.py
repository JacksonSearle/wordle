from bots.bot import Bot


class GreedyBot(Bot):
    def __init__(self):
        super().__init__()
        self.knowledge = {}

    def guess(self, game_state):
        return 'chimp'
    
    def record(self, game_state):
        pass
