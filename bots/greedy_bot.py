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
        for guess, feedback in game_state:
            key = (tuple(guess), tuple(feedback))
            if key not in temp:
                break
            temp = temp[key]
        if temp:
            (guess, feedback), _ = next(iter(temp.items()))
            guess = ''.join(guess)
            return guess
        else:
            return None
        
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
            avg_guess = self.avg_guess(guess, cur_answers)
            avg_guesses.append(avg_guess)
        for answer in cur_answers:
            index = self.guesses.index(answer)
            avg_guesses[index] *= (len(cur_answers) - 1) / len(cur_answers)
        best_word = self.guesses[avg_guesses.index(min(avg_guesses))]
        return best_word
    
    def get_cur_answers(self):
        cur_answers = []
        for answer in self.answers:
            success = True
            for guess, feedback in self.game_state:
                #TODO: make a quick_feedback function
                if self.get_feedback(guess, answer) != feedback:
                    success = False
                    break
            if success:
                cur_answers.append(answer)
        return cur_answers

    def avg_guess(self, guess, cur_answers):
        # Count the number of times each feedback occurs
        counter = {}
        for answer in cur_answers:
            feedback = tuple(self.get_feedback(guess, answer))
            if feedback not in counter:
                counter[feedback] = 0
            counter[feedback] += 1
        # Find the average of the values
        total = 0
        for key in counter:
            total += counter[key]
        avg = total / len(counter)
        return avg

