import game
import stringDatabase
import random
import re


class guess:
    def game(self):
        gamequit = False
        wordToGuess = "nave"  # stringDatabase.database.getWord(stringDatabase.database)
        currentGuess = list("----")
        score = 0
        badguess = 0
        missedletter = 0
        status = ""
        print(wordToGuess)
        while gamequit != True:
            if ('-' not in currentGuess):
                status = "success"
                game.game.gameList.append(game.game(wordToGuess, status, badguess, missedletter, score))
                wordToGuess = stringDatabase.database.getWord(stringDatabase.database)
                currentGuess = list("----")
                badguess = 0
                missedletter = 0
                score = 0
                status = ""
            print("Current guess is")
            print(''.join(currentGuess))
            print("wordToGuess is ", wordToGuess)
            print("g = guess, t = tellme, l for a letter, and q to quit")
            choice = str(input())
            if choice == "q":
                print("Quiting the game")
                game.game.gameList.append(game.game(wordToGuess, "Gave Up", badguess, missedletter, score))
                game.game.printGameList(game.game);
                gamequit = True
            if choice == "t":
                print("word is " + wordToGuess)
                wordToGuess = stringDatabase.database.getWord(stringDatabase.database)
                currentGuess = list("----")
                badguess = 0
                missedletter = 0
            if choice == "l":
                print("please enter the letter")
                letter = input()[0]
                characterscore = game.game.getScore(game.game, letter)
                if letter in wordToGuess and letter not in currentGuess:
                    # ref :https://stackoverflow.com/questions/3873361/finding-multiple-occurrences-of-a-string-within-a-string-in-python
                    for index in re.finditer(letter, str(wordToGuess)):
                        score = score + characterscore
                        currentGuess[index.start()] = letter
                else:
                    score = score - characterscore;
                    missedletter = missedletter + 1
            if choice == "g":
                print("please enter your guessed string")
                guessedstring = input()
                if guessedstring == wordToGuess:
                    print("your guess is correct")
                    wordToGuess = stringDatabase.database.getWord(stringDatabase.database)
                    currentGuess = list("----")
                else:
                    badguess = badguess + 1
                    score = score - (score) * 0.10
                    print("your guess is not correct")


guess.game(guess)
