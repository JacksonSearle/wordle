from bot import Bot

class Game():
    def __init__(self):
        self.bot = Bot()
        self.load_answers()

    def load_answers(self):
        self.answers = ['chimp']

    def play(self, answer):
        game_state = []
        for turn in range(6):
            guess = self.take_turn(game_state)
            game_state.append(guess)
            if guess == answer:
                return True
        return False

    def take_turn(self, game_state):
        return self.bot.guess(game_state)
    
    def test(self):
        for answer in self.answers:
            if self.play(answer) == False:
                return False
        return True