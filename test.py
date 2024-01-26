from game import Game

def main():
    game = Game()
    if game.test():
        print('All tests passed!')
    else:
        print('Tests failed!')

if __name__ == '__main__':
    main()