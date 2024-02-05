from utils import load, get_feedback


class Bot():
    def __init__(self, subset):
        self.load_guesses()
        self.get_feedback = get_feedback
        self.knowledge = {}
        self.subset = subset
    
    def load_guesses(self):
        self.guesses = load(f'words/guesses{self.subset}.pkl')
        self.answers = load(f'words/answers{self.subset}.pkl')

    def guess(self, game_state):
        pass