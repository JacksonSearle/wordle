from utils import load


class Game():
    def __init__(self, Bot, train=False):
        if train:
            self.bot = Bot
        else:
            self.bot = load(Bot.__class__.__name__)
        self.load_answers()

    def load_answers(self):
        self.answers = ['chimp']

    def play(self, answer):
        game_state = []
        for turn in range(6):
            guess = self.take_turn(game_state)
            feedback = self.get_feedback(guess, answer)
            game_state.append((guess, feedback))
            if guess == answer:
                return game_state, True
        return game_state, False

    def take_turn(self, game_state):
        return self.bot.guess(game_state)
    
    def test(self):
        for answer in self.answers:
            _, won = self.play(answer)
            if not won:
                return False
        return True
    
    def train(self):
        for answer in self.answers:
            game_state, won = self.play(answer)
            self.bot.record(game_state)
    
    def manually_use_bot(self):
        # Play the game
        print('\n\n\n\n\n')
        print('Welcome to Wordle!')
        print('The bot will hopefully guess the answer in 6 turns or less.')
        print(f'You have chosen {self.bot.__class__.__name__}.')
        game_state = []
        for turn in range(6):
            print(f'\nTurn {turn + 1}')
            guess = self.bot.guess(game_state)
            # Get user input for the game state
            print(f'Guess "{guess}"')
            feedback = self.get_user_feedback()
            game_state.append((guess, feedback))
            if feedback == 'GGGGG':
                print('You win!')
                return
        print('You lose!')

    def get_user_feedback(self):
        feedback_prompt = 'Type in Wordle\'s output. B for blank, Y for yellow, G for green like so: "GGYBB"\n'
        feedback = input(feedback_prompt)
        while not self.valid_feedback(feedback):
            feedback = input(feedback_prompt)
        return feedback
    
    def valid_feedback(self, feedback):
        return len(feedback) == 5 and all([letter in 'BGY' for letter in feedback])
    
    def get_feedback(self, guess, solution):
        feedback = []
        taken = []
        for gv, sv in zip(guess, solution):
            if gv is sv:
                feedback.append("G")
                taken.append("T")
            else:
                feedback.append("?")
                taken.append("?")
        for i in range(5):
            for j in range(5):
                if guess[i] is solution[j] and i != j and taken[j] != "T" and feedback[i] == "?":
                    feedback[i] = "Y"
                    taken[j] = "T"
        for i in range(len(feedback)):
            if feedback[i] == "?" or feedback[i] == "C":
                feedback[i] = "B"
        return feedback
