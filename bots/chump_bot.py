from bots.bot import Bot


class ChumpBot(Bot):
    def __init__(self, subset):
        super().__init__(subset)

    def guess(self, game_state):
        return 'chump'
    
    def record(self, game_state):
        pass
