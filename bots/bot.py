from utils import load, get_feedback


class Bot():
    def __init__(self):
        self.load_guesses()
        self.get_feedback = get_feedback
        self.knowledge = {}
    
    def load_guesses(self):
        self.guesses = load('words/guesses.pkl')
        self.answers = load('words/answers.pkl')

    def guess(self, game_state):
        pass