from bots.bot import Bot


class GreedyBot(Bot):
    def __init__(self):
        super().__init__()

    def guess(self, game_state):
        self.game_state = game_state
        guess = self.get_knowledge(game_state)
        if guess is not None:
            return guess
        else:
            return self.calculate_guess()
        
    def get_knowledge(self, game_state):
        temp = self.knowledge
        if temp == {}:
            return None
        for guess, feedback in game_state:
            key = (tuple(guess), tuple(feedback))
            if key not in temp:
                return None
            temp = temp[key]
            if temp == {}:
                return None
        return temp
        
    def record(self, game_state):
        temp = self.knowledge
        for guess, feedback in game_state:
            key = (tuple(guess), tuple(feedback))
            if key not in temp:
                temp[key] = {}
            temp = temp[key]

    def calculate_guess(self):
        cur_answers = self.get_cur_answers()
        avg_guesses = []
        for guess in self.guesses:
            num = self.avg_guess(guess, cur_answers)
            avg_guesses.append(num)
        for answer in cur_answers:
            index = self.guesses.index(answer)
            avg_guesses[index] *= (len(cur_answers) - 1) / len(cur_answers)
        best_word = self.guesses[avg_guesses.index(min(avg_guesses))]
        return best_word
    
    def get_cur_answers(self):
        cur_answers = []
        for answer in self.answers:
            for guess, feedback in self.game_state:
                #TODO: make a quick_feedback function
                if self.get_feedback(guess, answer) != feedback:
                    break
            cur_answers.append(answer)
        return cur_answers

    def avg_guess(self, guess, cur_answers):
        num_left = []
        for _, feedback in self.game_state:
            count = 0
            for answer in cur_answers:
                if self.get_feedback(guess, answer) == feedback:
                    count += 1
            num_left.append(count)
        avg = 0
        summation = sum(num_left)
        for num in num_left:
            avg += (num / summation) * num
        return avg

