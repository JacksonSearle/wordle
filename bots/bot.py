from utils import load


class Bot():
    def __init__(self):
        self.load_guesses()
    
    def load_guesses(self):
        self.guesses = load('words/guesses.pkl')
        self.answers = load('words/answers.pkl')

    def guess(self, game_state):
        pass