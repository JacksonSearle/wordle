import pickle

def save(object, path):
    # Pickle this object
    pickle.dump(object, open(path, 'wb'))

def load(path):
    # Load the pickled object
    return pickle.load(open(path, 'rb'))

def get_feedback(guess, answer):
    feedback = []
    taken = []
    for gv, sv in zip(guess, answer):
        if gv is sv:
            feedback.append("G")
            taken.append("T")
        else:
            feedback.append("?")
            taken.append("?")
    for i in range(5):
        for j in range(5):
            if guess[i] is answer[j] and i != j and taken[j] != "T" and feedback[i] == "?":
                feedback[i] = "Y"
                taken[j] = "T"
    for i in range(len(feedback)):
        if feedback[i] == "?" or feedback[i] == "C":
            feedback[i] = "B"
    return feedback