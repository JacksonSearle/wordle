
# Wordle

## Introduction
This project features three bots for Wordle. Run bots in inference mode for help playing wordle.

## Bots Overview
### Greedy Bot
- **Performance**: On average, takes 3.43 turns to win.
- **Training Time**: Approximately a few minutes.
- **Strategy**: Minimizes average number of possible solutions left. Looks ahead one turn.

### Chump Bot
- **Performance**: Typically loses, averaging around 6 guesses.
- **Training Time**: Instantaneous.
- **Strategy**: Guesses 'Chump' every time.

### Random Bot
- **Performance**: Typically loses, averaging around 6 guesses.
- **Training Time**: Instantaneous.
- **Strategy**: Guesses a random possible solution.

## Getting Started

### Prerequisites
- Python 3.11.3

### Usage
1. **Training the Bots**
   Run `main.py` in 'train' mode to train the bots. 
   ```
   python main.py train
   ```
   Follow the prompt to select a bot to train.

2. **Testing the Bots**
   To test the bots, use 'test' mode.
   ```
   python main.py test
   ```
   Follow the prompt to select a bot to test.

3. **Inference**
   For running the bots in inference mode:
   ```
   python main.py inference
   ```
   Follow the prompt to select a bot for inference.
