from bots.bot import Bot

class Node():
    def __init__(self, name, info, states=None):
        self.name = name
        self.info = info
        self.parents = []
        self.children = []
        if states != None:
            states.append(self)
    
    def add_parent(self, parent):
        self.parents.append(parent)

    def add_child(self, child):
        self.children.append(child)

class BestBot(Bot):
    def __init__(self):
        super().__init__()
        self.states = []
        self.root = Node('state', self.answers, self.states)

    def guess(self, game_info):
        guess = self.get_knowledge(game_info)
        if guess == None:
            return self.calculate_guess()
        else:
            return guess
    
    def get_knowledge(self, game_info):
        temp_game_info = game_info.copy()
        while len(temp_game_info) >= 0:
            for state in self.states:
                if state.info  == self.get_cur_state(temp_game_info):
                    return state
            temp_game_info.pop()
        return None
    
    def record(self, game_info):
        # Record the path from the root to the current state
        pass

    def calculate_guess(self, root):
        # Calculate one step forward in the knowledge tree
        self.guess_nodes()
        self.feedback_nodes()
        self.state_nodes()
        pass

    def guess_nodes(self, root):
        # These nodes represent a future guess that could be taken
        # These nodes are the children of the current state node
        # Iterate through each guess
        for guess in self.guesses:
            # Create a guess node
            # Add the guess node to the current state node
        pass

    def feedback_nodes(self, root):
        # These nodes represent the feedback that could be received
        # These nodes are the children of the guess nodes
        pass

    def state_nodes(self):
        # These nodes represent the state of the game after a guess and feedback
        # These nodes are the children of the feedback nodes
        # There are not duplicates of state_nodes, unique ones are shared between feedback nodes
        # Add all states to self.states
        pass

    def get_cur_state(self):
        cur_state = []
        for answer in self.answers:
            success = True
            for guess, feedback in self.game_info:
                #TODO: make a quick_feedback function
                if self.get_feedback(guess, answer) != feedback:
                    success = False
                    break
            if success:
                cur_state.append(answer)
        return cur_state