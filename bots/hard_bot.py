from bots.bot import Bot


class HardBot(Bot):
    def __init__(self, subset):
        super().__init__(subset)

    def guess(self, game_state):
        return 'modes'
    
    def record(self, game_state):
        pass
