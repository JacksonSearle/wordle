from bots.bot import Bot


class GreedyBot(Bot):
    def __init__(self):
        super().__init__()

    def guess(self, game_state):
        self.game_state = game_state
        return 'chimp'
    
    def record(self, game_state):
        pass

    def calculate_guess(self):
        cur_solutions = self.get_cur_solutions()
        avg_guesses = []
        for guess in self.guesses:
            num = self.avg_guess(guess)
            avg_guesses.append(num)
        for solution in cur_solutions:
            index = self.guesses.index(solution)
            avg_guesses[index] *= (len(cur_solutions) - 1) / len(cur_solutions)
        best_word = self.guesses[avg_guesses.index(min(avg_guesses))]
        return best_word
    
    def get_cur_solutions(self, guess):
        cur_solutions = []
        for solution in self.solutions:
            for _, feedback in self.game_state:
                #TODO: make a quick_feedback function
                if self.get_feedback(guess, solution) == feedback:
                    cur_solutions.append(solution)
        return cur_solutions

    def avg_guess(self, guess, curr_solutions, feedbacks):
        num_left = []
        for feedback in feedbacks:
            count = 0
            for solution in curr_solutions:
                if self.get_feedback(guess, solution) == feedback:
                    count += 1
            num_left.append(count)
        avg = 0
        summation = sum(num_left)
        for num in num_left:
            avg += (num / summation) * num
        return avg

