import pickle

def save(object, path):
    # Pickle this object
    pickle.dump(object, open(path, 'wb'))

def load(path):
    # Load the pickled object
    return pickle.load(open(path, 'rb'))