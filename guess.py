import stringDatabase
import random
import re


class guess:
    def game(self):
        gamequite = False
        wordToGuess = list(stringDatabase.database.getWord(stringDatabase.database))
        currentGuess = list("----")
        print(wordToGuess)
        while gamequite != True:

            print("Current guess is")
            print(''.join(currentGuess))
            print("g= guess, t = tellme, l for a letter, and q to quit")
            choice = str(input())
            if choice == "q":
                print("Quiting the game")
                gamequite = True
            if choice == "l":
                letter = input()[0]
                if letter in wordToGuess:
                    print("your one character is correct")
                    indexToChange = wordToGuess.index(letter)
                    currentGuess[indexToChange] = letter
                    for m in re.finditer(letter, wordToGuess):
                        print('ll found', m.start(), m.end())


guess.game(guess)
