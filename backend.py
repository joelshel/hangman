#!/usr/bin/env python3

# this is an old and small database 
# words = ('word', 'choice', 'random', 'hello', 'house', 'correct', 'programmer', 'juice', 'cookies', 'chocolate', 'world', 'home', 'welcome', 'wrong', 'scarf', 'attack', 'defense', 'accuracy', 'string', 'integer', 'float', 'risk', 'beautiful', 'sad', 'candle', 'connection', 'risky', 'runner', 'closet', 'mariage')

# words database from https://github.com/Xethron/Hangman/blob/master/words.txt

from random import choice
import string

def get_words(file):
    """A small function to get a tuple with the words of the game.

    Args:
        file (str): The name of the file in format txt (words separated by a \n).

    Returns:
        tuple of str: A tuple with all the words.
    """
    with open(file, "r") as f:
        raw_words = f.readlines()

    words = ()
    for word in raw_words:
        words += (word.strip(),)
    return words

words = get_words(file="words.txt")

lives = 6

class Game():    
    def __init__(self, words):
        """__init__ function. Defines the alphabet and the list of words of the game.

        Args:
            words (tuple or List): A tuple or list of words.keys
        """
        self.words = words
        self.alphabet = set(string.ascii_uppercase)


    def choose_word(self):
        """Function to choose the word.
        """
        self.word = choice(self.words).upper()

    
    def set_word_letters(self):
        """Function that defines the sets with the used letters and the word letters.
        """
        self.word_letters = set(self.word)
        self.used_letters = set()


    def start_game(self, lives):
        """Core of the game. If called you can play the game once.

        Args:
            lives (int): The hangman lives.
        """
        self.lives = lives
        while len(self.word_letters) > 0 and self.lives > 0:
            print(f'You have {self.lives} lives remaining.')
            print('Used letters:' + ' '.join(self.used_letters))
            word_list = [letter if letter in self.used_letters else '_' for letter in self.word]
            print('Word: ' + ' '.join(word_list))
            user_letter = input('Enter a letter: ').upper()
            if user_letter in self.alphabet - self.used_letters:
                self.used_letters.add(user_letter)
                if user_letter in self.word_letters:
                    self.word_letters.remove(user_letter)
                else:
                    self.lives -= 1
            elif user_letter in self.used_letters:
                print('You already used that letter. Try again.')
            else:
                print('Enter a valid letter.')
            print()
        if self.lives > 0:
            print(f'Congratulations, you guessed the word {self.word}!')
        else:
            print(f'Oh, you lose! Try again. The word were {self.word}!')


    def game_loop(self, lives, flag=1):
        """A method to play the game in a loop as many times as you like.

        Args:
            lives (int): The hangman lives.
            flag (int, optional): A flag to restart the loop. Defaults to 1.
        """
        if flag:
            self.choose_word()
            self.set_word_letters()
            self.start_game(lives)
        answer = input("Do you want to play again? [Y/N]: ")[0].upper()
        if answer == "Y":
            self.game_loop(lives)
        elif answer == "N":
            print("See you later!")
        else:
            print("Type a valid answer!")
            self.game_loop(lives, flag=0)


if __name__=='__main__':
    game = Game(words)
    game.game_loop(lives)
