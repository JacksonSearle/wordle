import random
from bots.bot import Bot


class RandomBot(Bot):
    def __init__(self, subset):
        super().__init__(subset)

    def guess(self, game_state):
        return random.choice(self.answers)
    
    def record(self, game_state):
        pass