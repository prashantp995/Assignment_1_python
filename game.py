"""
      word frequency table
"""
scoreTable = {
    'a': 8.17, 'b': 1.49, 'c': 2.78,
    'd': 4.25, 'e': 12.07, 'f': 2.23, 'g': 2.02, 'h': 6.09,
    'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
    'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97,
    'z': 0.07
}
# Columns for the printing final result
Column = [
    "Game", "Word", "Status", "Bad Guess", "Missed Letters", "Score"
]

"""
     This class will store data regarding game and contains method to print all stored values
"""


class game:
    # each game's statistics will be stored in this game list
    gameList = []

    def __init__(self, word=None, status=None, badguess=None, missedletters=None, score=None):
        """
        Constructor
        :rtype: object of game class
        :param badguess: number of bad guess during game for given word
        :param missedletters: number of missed letters
        :param score: score for the game (for particular word)
        :param word :word in current game
        :param status : status of the game
        """
        self.word = word
        self.status = status
        self.badguess = badguess
        self.missedletters = missedletters
        self.score = score

    def getScore(self, character):
        """
        This function will return score for the particular character
        :param character: input character for which score is needed
        :rtype: object
        """
        return scoreTable.get(character.lower())

    def printGameList(self):
        """
        this functions prints each game's statistics
        """
        # ref :https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically
        # ref :https://www.tutorialspoint.com/python/string_ljust.htm
        counter = 0
        totalscore = 0.0
        for game in self.gameList:
            if (counter == 0):
                for col in Column:
                    print(col.ljust(20), end="");
                print("\n")
            printscore = f'{game.score:.3f}' # need to get precision up to 3 points
            print(f'{str(counter).ljust(20)}', end="")
            print(f'{game.word.ljust(20)}', end="")
            print(f'{game.status.ljust(20)}', end="")
            print(f'{str(game.badguess).ljust(20)}', end="")
            print(f'{str(game.missedletters).ljust(20)}', end="")
            print(f'{str(printscore).ljust(20)}', end="")
            counter = counter + 1
            totalscore = totalscore + game.score
            print("\n")
        print(f'final score :{totalscore:.3f}')
