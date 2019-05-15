wordFrequency = {'a': 8.17,
                 'b': 1.49,
                 'c': 2.78,
                 'd': 4.25,
                 'e': 12.70,
                 'f': 2.23,
                 'g': 2.02,
                 'h': 6.09,
                 'i': 6.97,
                 'j': 0.15,
                 'k': 0.77,
                 'l': 4.03,
                 'm': 2.41,
                 'n': 6.75,
                 'o': 7.51,
                 'p': 1.93,
                 'q': 0.10,
                 'r': 5.99,
                 's': 6.33,
                 't': 9.06,
                 'u': 2.76,
                 'v': 0.98,
                 'w': 2.36,
                 'x': 0.15,
                 'y': 1.97,
                 'z': 0.07
                 }


class game:
    gameList = []

    def __init__(self, word=None, status=None, badguess=None, missedletters=None, score=None):
        self.word = word
        self.status = status
        self.badguess = badguess
        self.missedletters = missedletters
        self.score = score

    def getScore(self, input):
        print("getting score for ", input)
        return 100 - wordFrequency.get(input.lower())

    def printGameList(self):
        print("Game     word        status      Bad guess      missedletters                score")
        # ref :https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically
        counter = 0
        for game in self.gameList:
            print(counter, end="")
            print("\t\t", game.word, end=" ")
            print("\t\t", game.status, end=" ")
            print("\t\t\t\t", game.badguess, end=" ")
            print("\t\t\t\t\t", game.missedletters, end=" ")
            print("\t\t\t\t\t", game.score, end=" ")
            counter = counter + 1
            print("\n")
