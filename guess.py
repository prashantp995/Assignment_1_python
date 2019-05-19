import re

import game
import stringDatabase

"""
    This class contains logic for playing game.
"""


class guess:
    """
          Init the game.
          For bad guess , 10% penalty will be applied on current total score
          For missed character , 50 % of missed character's score penalty will be applied
          For give up , every '-' in current guess , penalty will be applied
    """

    def game(self):
        # init variables
        gamequit = False
        wordToGuess = stringDatabase.database.getWord(stringDatabase.database)
        currentGuess = list("----")
        score = 0
        badGuess = 0
        missedLetter = 0
        gameCounter = 0
        status = ""
        while gamequit != True:
            if ('-' not in currentGuess):
                status = "success"
                # add game details to game list
                game.game.gameList.append(game.game(wordToGuess, status, badGuess, missedLetter, score))
                wordToGuess = stringDatabase.database.getWord(stringDatabase.database)
                currentGuess = list("----")
                badGuess = 0
                missedLetter = 0
                score = 0
                status = ""
                print(
                    "----------------------------------Now guess the next word in the game-----------------------------------")
            print("Current guess is")
            print(''.join(currentGuess))
            print("g = guess, t = tellme, l for a letter, and q to quit")
            if (gameCounter > 100):
                print("you have played 100 rounds")
                game.game.printGameList(game.game)
                gamequit = True
                currentGuess = list("----")
                badGuess = 0
                missedLetter = 0
                score = 0
            choice = str(input())
            gameCounter = gameCounter + 1
            if choice == "q":
                print("Quiting the game")
                game.game.printGameList(game.game)
                gamequit = True
                currentGuess = list("----")
                badGuess = 0
                missedLetter = 0
                score = 0
            if choice == "t":
                print("word is " + wordToGuess)
                print("your current guess is ", ''.join(currentGuess))
                print("score will be deducted for each '-' in the current guess")
                for index in re.finditer('-', ''.join(currentGuess)):
                    score = score - game.game.getScore(game.game, wordToGuess[index.start()])
                game.game.gameList.append(game.game(wordToGuess, "Gave Up", badGuess, missedLetter, score))
                wordToGuess = stringDatabase.database.getWord(stringDatabase.database)
                currentGuess = list("----")
                badGuess = 0
                missedLetter = 0
                score = 0
                print(
                    "----------------------------------Now guess the next word in the game-----------------------------------")
            if choice == "l":
                print("please enter the letter")
                tempInput = input()
                if (tempInput != ""):
                    letter = tempInput[0]
                characterscore = game.game.getScore(game.game, letter)
                if letter in wordToGuess and letter not in currentGuess:
                    # ref :https://stackoverflow.com/questions/3873361/finding-multiple-occurrences-of-a-string-within-a-string-in-python
                    for index in re.finditer(letter, str(wordToGuess)):
                        score = score + characterscore
                        currentGuess[index.start()] = letter
                else:
                    score = score - (characterscore) * 0.50
                    missedLetter = missedLetter + 1
            if choice == "g":
                print("please enter your guessed string")
                guessedString = input()
                if guessedString == wordToGuess:
                    print("your guess is correct")
                    tempscore = 0
                    for character in wordToGuess:
                        tempscore = tempscore + game.game.getScore(game.game, character)
                    game.game.gameList.append(game.game(wordToGuess, "Success", badGuess, missedLetter, tempscore))
                    wordToGuess = stringDatabase.database.getWord(stringDatabase.database)
                    currentGuess = list("----")
                    badGuess = 0
                    missedLetter = 0
                    score = 0
                    status = ""
                    print(
                        "----------------------------------Now guess the next word in the game-----------------------------------")
                else:
                    badGuess = badGuess + 1
                    score = score - (score) * 0.10
                    print("your guess is not correct ")


guess.game(guess)
