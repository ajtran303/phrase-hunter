# Phrase Hunter

Project 3 of the Treehouse Python TechDegree

## Features

- Object-Oriented Programming!
  - The Phrase class displays underscores or letters depending on player guesses
  - The Game class tracks user's guesses, misses, and if a player won or lost

- Validations for user inputs!
  - Pretty and kind messages for invalid inputs
  - Including a pretty message for quitting out with a `KeyboardInterrupt`

- Play multiple games!
  - The game itself is started by one instance of the Game class
  - Starting a new game creates a new Game instance

## Installing the project

Clone this repo and navigate into the `phrase-hunter` project directory.

```zsh
git clone https://github.com/ajtran303/phrase-hunter.git
cd phrase-hunter
```

## Starting the game

### Mac:

```zsh
python3 app.py
```

### Windows / Linux:

```zsh
python app.py
```

## Playing the game

You will be prompted with the rules:

```zsh
Welcome to the Phrase Hunting game!
- Win by guessing all the letters!!
- Lose by missing five (5) guesses!
- Quit with `<control>+C` or `<control>+D`
```

A valid guess is a single letter from the English Alphabet. Case doesn't matter.


## Modding the game

You can modify the class variable, `Game.phrases` to hunt different phrases.

Follow the examples there:

```python
class Game():
    phrases = [
        Phrase('Hello World'),
        Phrase('Hello Mother'),
        Phrase('Hello Father'),
        Phrase('Here I am at'),
        Phrase('Camp Granada'),
    ]
```

### Constraints for creating Phrases

- There are five but it can be modified to have as many or as little as desired!
- Phrases must be a string of at least one word made of only letters and spaces
- The program will throw an error with message when provided an invalid phrase
- The game will not start unless all phrases pass the validation checks

## Breaking the game

If you find a bug, please [report it to me](https://github.com/ajtran303/phrase-hunter/issues/new)!
