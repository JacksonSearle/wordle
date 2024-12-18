from tqdm import tqdm
from utils import load, save, get_feedback, print_memory_usage
from bots.chump_bot import ChumpBot
from bots.random_bot import RandomBot
from bots.greedy_bot import GreedyBot
from bots.best_bot import BestBot
import time


class Game():
    def __init__(self,mode='inference', subset=None):
        self.subset = subset
        if mode == 'subset':
            self.create_subset()
            return
        self.load_answers()
        Bot = self.select_bot()
        if mode == 'train':
            self.bot = Bot
            self.train()
            if subset:
                save(self.bot, f'bots/saved/{self.bot.__class__.__name__}{subset}.pkl')
            else:
                save(self.bot, f'bots/saved/{self.bot.__class__.__name__}.pkl')
        else:
            if subset:
                self.bot = load(f'bots/saved/{Bot.__class__.__name__}{subset}.pkl')
            else:
                self.bot = load(f'bots/saved/{Bot.__class__.__name__}.pkl')
            if mode == 'test':
                self.test()
            elif mode == 'inference':
                self.inference()

    def create_subset(self):
        # Load answers.pkl and guesses.pkl and save a subset of them
        answers = load('words/answers.pkl')
        guesses = load('words/guesses.pkl')

        # Randomly select self.subset percent of the data
        num_answers = len(answers)
        num_guesses = len(guesses)

        subset_answers = answers[:int(num_answers * float(self.subset))]
        subset_guesses = guesses[:int(num_guesses * float(self.subset))]

        # Save the subsets
        save(subset_answers, f'words/answers{self.subset}.pkl')
        save(subset_guesses, f'words/guesses{self.subset}.pkl')

    def select_bot(self):
        bots = [ChumpBot, RandomBot, GreedyBot, BestBot]

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

        bot = bots[int(selection)](self.subset)
        
        return bot

    def load_answers(self):
        if self.subset:
            self.answers = load(f'words/answers{self.subset}.pkl')
        else:
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
        wins = 0
        for answer in self.answers:
            game_state, won = self.play(answer)
            turns_taken = len(game_state)
            total_turns += turns_taken
            max_turns = max(max_turns, turns_taken)
            if won:
                wins += 1
        num_answers = len(self.answers)
        average_turns = round(total_turns / num_answers, 2)
        win_percentage = round((wins / num_answers) * 100, 2)
        print(f'Average turns needed to win: {average_turns}')
        print(f'Highest number of turns taken: {max_turns}')
        print(f'Win percentage: {win_percentage}%')
    
    def train(self):
        start = time.time()
        for answer in tqdm(self.answers):
            game_state = []
            for turn in range(6):
                guess = self.take_turn(game_state)
                #! Take away this breakpoint
                break
                feedback = get_feedback(guess, answer)
                game_state.append((guess, feedback))
                self.bot.record(game_state)
                if guess == answer:
                    break
        end = time.time()
        print(f'Training took {round(end - start, 2)} seconds.')
        # Print out how many nodes were created
        print(f'Number of nodes created: {self.bot.num_nodes}')
        # Print out how many gigs of memory were used
        print_memory_usage()
    
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
