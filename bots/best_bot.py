from bots.bot import Bot

class BestBot(Bot):
    def __init__(self):
        super().__init__()

    def guess(self, game_state):
        return 'super'
    
    def record(self, game_state):
        pass