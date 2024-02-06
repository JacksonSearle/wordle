import sys
from utils import *
from game import Game


def main():
    # Set mode to train, test, or inference based on command line argument
    mode = sys.argv[1] if len(sys.argv) > 1 else 'test'
    subset = sys.argv[2] if len(sys.argv) > 2 else None
    if mode not in ['train', 'test', 'inference', 'subset']:
        print("Usage: python main.py [train|test|inference|subset] [subset]")
        return
    Game(mode=mode, subset=subset)

if __name__ == '__main__':
    main()