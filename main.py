import sys
from utils import *
from game import Game


def main():
    # Set mode to train, test, or inference based on command line argument
    mode = sys.argv[1] if len(sys.argv) > 1 else 'test'
    if mode not in ['train', 'test', 'inference']:
        print("Usage: python main.py [train|test|inference]")
        return
    Game(mode=mode)

if __name__ == '__main__':
    main()