import stringDatabase
import random
import re


class guess:
    def game(self):
        gamequit = False
        wordToGuess = stringDatabase.database.getWord(stringDatabase.database)
        currentGuess = list("----")
        print(wordToGuess)
        while gamequit != True:

            print("Current guess is")
            print(''.join(currentGuess))
            print("g = guess, t = tellme, l for a letter, and q to quit")
            choice = str(input())
            if choice == "q":
                print("Quiting the game")
                gamequit = True
            if choice == "t":
                print("word is " + wordToGuess)
                wordToGuess = stringDatabase.database.getWord(stringDatabase.database)
                currentGuess = list("----")
            if choice == "l":
                letter = input()[0]
                if letter in wordToGuess:
                    print("your one character is correct")
                    # ref :https://stackoverflow.com/questions/3873361/finding-multiple-occurrences-of-a-string-within-a-string-in-python
                    for index in re.finditer(letter, str(wordToGuess)):
                        currentGuess[index.start()] = letter


guess.game(guess)
