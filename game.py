from tqdm import tqdm
from utils import load, save, get_feedback
from bots.chump_bot import ChumpBot
from bots.random_bot import RandomBot
from bots.greedy_bot import GreedyBot


class Game():
    def __init__(self,mode='inference'):
        self.load_answers()
        Bot = self.select_bot()
        if mode == 'train':
            self.bot = Bot
            self.train()
            save(self.bot, f'bots/saved/{self.bot.__class__.__name__}.pkl')
        else:
            self.bot = load(f'bots/saved/{Bot.__class__.__name__}.pkl')
            if mode == 'test':
                self.test()
            elif mode == 'inference':
                self.inference()

    def select_bot(self):
        bots = [ChumpBot, RandomBot, GreedyBot]

        # Print out each class name
        print('Select a bot:')
        for i, bot in enumerate(bots):
            print(f'{i}: {bot.__name__}')

        # Get user input
        while True:
            selection = input()
            if selection.isdigit() and int(selection) in range(len(bots)):
                break
            else:
                print('Invalid selection. Please try again.')

        bot = bots[int(selection)]()
        
        return bot

    def load_answers(self):
        self.answers = load('words/answers.pkl')

    def play(self, answer):
        game_state = []
        for turn in range(6):
            guess = self.take_turn(game_state)
            feedback = get_feedback(guess, answer)
            game_state.append((guess, feedback))
            if guess == answer:
                return game_state, True
        return game_state, False

    def take_turn(self, game_state):
        return self.bot.guess(game_state)
    
    def test(self):
        print(f'\nTesting {self.bot.__class__.__name__}...')
        total_turns = 0
        max_turns = 0
        for answer in self.answers:
            game_state, won = self.play(answer)
            turns_taken = len(game_state)
            total_turns += turns_taken
            max_turns = max(max_turns, turns_taken)
            if not won:
                print(f'Failed to win with answer: {answer}')
        num_answers = len(self.answers)
        average_turns = total_turns / num_answers
        print(f'Average turns needed to win: {average_turns}')
        print(f'Most amount of turns taken: {max_turns}')
    
    def train(self):
        for answer in tqdm(self.answers):
            game_state = []
            for turn in range(6):
                guess = self.take_turn(game_state)
                feedback = get_feedback(guess, answer)
                game_state.append((guess, feedback))
                self.bot.record(game_state)
                if guess == answer:
                    break
    
    def inference(self):
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
