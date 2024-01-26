class Game():
    def __init__(self, Bot):
        self.bot = Bot
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
            feedback = self.get_feedback()
            game_state.append((guess, feedback))
            if feedback == 'GGGGG':
                print('You win!')
                return
        print('You lose!')

    def get_feedback(self):
        feedback_prompt = 'Type in Wordle\'s output. B for blank, Y for yellow, G for green like so: "GGYBB"\n'
        feedback = input(feedback_prompt)
        while not self.valid_feedback(feedback):
            feedback = input(feedback_prompt)
        return feedback
    
    def valid_feedback(self, feedback):
        return len(feedback) == 5 and all([letter in 'BGY' for letter in feedback])