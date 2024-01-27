from bots.bot import Bot

class Node():
    def __init__(self, name, info, states=None, parent=None):
        self.name = name
        self.info = info
        self.parents = []
        self.children = []
        self.guess = None
        if parent != None:
            self.add_parent(parent)
        if states != None:
            states[self.info] = self
    
    def add_parent(self, parent):
        self.parents.append(parent)
        parent.children.append(self)

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)

class BestBot(Bot):
    def __init__(self):
        super().__init__()
        self.states = {}
        self.root = Node('state', self.answers, self.states)

    def guess(self, game_info):
        state = self.get_knowledge(game_info)
        if state.guess:
            return state.guess
        else:
            return self.calculate_guess(state)
    
    def get_knowledge(self, game_info):
        temp_game_info = game_info.copy()
        while len(temp_game_info) >= 0:
            state = self.get_cur_state(temp_game_info)
            if state in self.states:
                return state
            temp_game_info.pop()
        return None
    
    def record(self, game_info):
        # Add game_info to knowledge like how greedy_bot does it
        pass

    def calculate_guess(self, root):
        # Calculate one step forward in the knowledge tree
        self.guess_nodes(root)
        pass

    def guess_nodes(self, state_node):
        for guess in self.guesses:
            guess_node = Node('guess', guess, parent=state_node)
            self.feedback_nodes(guess_node)

    def feedback_nodes(self, guess_node):
        # These nodes represent the feedback that could be received
        # These nodes are the children of the guess nodes
        # Find all possible feedbacks
        # Go through every answer
        feedback_nodes = []
        for answer in self.answers:
            feedback = self.get_feedback(guess_node.info, answer)
            feedback_node = Node('feedback', feedback, parent=guess_node)
            feedback_nodes.append(feedback_node)

        self.state_nodes(feedback_nodes)

    def state_nodes(self, feedback_nodes):
        # These nodes represent the state of the game after a guess and feedback
        # These nodes are the children of the feedback nodes
        # There are not duplicates of state_nodes, unique ones are shared between feedback nodes
        # Add all states to self.states
        for feedback_node in feedback_nodes:
            cur_state = self.update_state(feedback_node)
            # Check if state_node is already in self.states
            found = False
            if cur_state in self.states:
                state = self.states[cur_state]
                feedback_node.add_child(state)
            else:
                Node('state', cur_state, self.states, parent=feedback_node)

    def update_state(self, feedback_node):
        # Given a feedback node, update the state of the game
        # This goes up through the feedback_node's parents
        # So it goes to the guess_node then the state_node
        # From the state_node, it gets the state of the game
        # Then it updates the state of the game based on the guess and feedback
        # Then it returns the new state
        if len(feedback_node.parents) > 1 or len(feedback_node.parents) <= 0:
            raise Exception('Feedback node has more than one parent or no parents')
        if len(guess_node.parents) > 1 or len(guess_node.parents) <= 0:
            raise Exception('Guess node has more than one parent or no parents')
        
        guess_node = feedback_node.parents[0]
        state_node = guess_node.parents[0]

        old_state = state_node.info
        guess = guess_node.info
        feedback = feedback_node.info

        new_state = []
        for answer in old_state:
            if self.get_feedback(guess, answer) == feedback:
                new_state.append(answer)

        # TODO: Recurse???
        return new_state

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