from bots.bot import Bot

class BestBot(Bot):
    def __init__(self):
        super().__init__()

    def guess(self, game_state):
        # Decide if we need to calculate a new guess
        self.get_cur_answers()
        guess = self.get_knowledge()
        if guess == None:
            return self.calculate_guess()
        else:
            return guess
    
    def get_knowledge(self):
        pass
    
    def record(self, game_state):
        pass

    def calculate_guess(self, cur_answers):
        # Calculate one step forward in the knowledge tree
        pass

    def get_cur_answers(self):
        pass