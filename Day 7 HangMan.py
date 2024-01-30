import random
import sys


def hangman_model(counter):
    pic_art = {
        0: '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''',
        1: '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
        2: '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
        3: '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''',
        4: '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    ''',
        5: '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    ''',
        6: '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    Game Over
    '''
    }
    print(pic_art[counter])


word_list = ["ardavark", "baboon", "camel"]
guess_word = random.choice(word_list)
print("Random word is {0}".format(guess_word))
underscore_list = []
for blank in range(len(guess_word)):
    underscore_list.append("_")
print(underscore_list)
guessed_letter = set()
hangman_counter = 0
while (hangman_counter < 6) and (''.join(map(str, underscore_list)) != guess_word):
    guess_letter = input("Please make a guess\t")
    guess_letter = guess_letter.lower()
    if guess_letter in guessed_letter:
        print("You guessed it")
        continue
    guessed_letter.add(guess_letter)
    found = False
    for index in range(len(guess_word)):
        if guess_letter == guess_word[index]:
            underscore_list[index] = guess_letter
            print(underscore_list)
            found = True
    if not found:
        hangman_counter += 1
        hangman_model(hangman_counter)
if hangman_counter == 6:
    hangman_model(counter=6)
    sys.exit()
