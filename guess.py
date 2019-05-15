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
                print("please enter the letter")
                letter = input()[0]
                if letter in wordToGuess:
                    print("your one character is correct")
                    # ref :https://stackoverflow.com/questions/3873361/finding-multiple-occurrences-of-a-string-within-a-string-in-python
                    for index in re.finditer(letter, str(wordToGuess)):
                        currentGuess[index.start()] = letter
            if choice == "g":
                print("please enter your guessed string")
                guessedstring = input()
                if guessedstring == wordToGuess:
                    print("your guess is correct")
                    wordToGuess = stringDatabase.database.getWord(stringDatabase.database)
                    currentGuess = list("----")
                else:
                    print("your guess is not correct")


guess.game(guess)
