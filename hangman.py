#!/usr/bin/env python3

# code from:
# https://www.youtube.com/watch?v=8ext9G7xspg&t=5s

words = ('word', 'choice', 'random', 'hello', 'house', 'correct', 'programmer', 'juice', 'cookies', 'chocolate', 'world', 'home', 'welcome', 'wrong', 'scarf', 'attack', 'defense', 'accuracy', 'string', 'integer', 'float', 'risk', 'beautiful', 'sad', 'candle', 'connection', 'risky', 'runner', 'closet', 'mariage')
from random import choice
import string
alphabet = set(string.ascii_uppercase)
word = choice(words).upper()
word_letters = set(word)
used_letters = set()
lives = 6
while len(word_letters) > 0 and lives > 0:
    print(f'You have {lives} lives remaining.')
    print('Used letters:' + ' '.join(used_letters))
    word_list = [letter if letter in used_letters else '_' for letter in word]
    print('Word: ' + ' '.join(word_list))
    user_letter = input('Enter a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        else:
            lives -= 1
    elif user_letter in used_letters:
        print('You already used that letter. Try again.')
    else:
        print('Enter a valid letter.')
    print()
if lives > 0:
    print(f'Congratulations, you guessed the word {word}!')
else:
    print(f'Oh, you lose! Try again. The word were {word}!')
