from utils import load, get_feedback


class Bot():
    def __init__(self, subset):
        self.subset = subset
        self.load_guesses()
        self.get_feedback = get_feedback
        self.knowledge = {}
        self.num_nodes = 0
    
    def load_guesses(self):
        if self.subset:
            self.guesses = load(f'words/guesses{self.subset}.pkl')
            self.answers = load(f'words/answers{self.subset}.pkl')
        else:
            self.guesses = load('words/guesses.pkl')
            self.answers = load('words/answers.pkl')

    def guess(self, game_state):
        pass