wordFrequency = {
    'a': 3,
    'b': 20,
    'c': 12,
    'd': 10,
    'e': 1,
    'f': 16,
    'g': 17,
    'h': 8,
    'i': 5,
    'j': 23,
    'k': 22,
    'l': 11,
    'm': 14,
    'n': 6,
    'o': 4,
    'p': 19,
    'q': 25,
    'r': 9,
    's': 7,
    't': 2,
    'u': 13,
    'v': 21,
    'w': 15,
    'x': 24,
    'y': 18,
    'z': 26
}
Column = [
    "Game",
    "Word",
    "Status",
    "Bad Guess",
    "Missed Letters",
    "Scores"
]


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
        return wordFrequency.get(input.lower())

    def printGameList(self):
        # print("Game\t\tword\t\tstatus\tBad guess\tmissedletters\t\t\tscore")

        # ref :https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically
        counter = 0
        for game in self.gameList:
            if (counter == 0):
                for col in Column:
                    print(col.ljust(20), end="");
                print("\n")
            print(f'{str(counter).ljust(20)}', end="")
            print(f'{game.word.ljust(20)}', end="")
            print(f'{game.status.ljust(20)}', end="")
            print(f'{str(game.badguess).ljust(20)}', end="")
            print(f'{str(game.missedletters).ljust(20)}', end="")
            print(f'{str(game.score).ljust(20)}', end="")
            counter = counter + 1
            print("\n")
