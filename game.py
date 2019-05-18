"""
      word frequency table , points are assigned based on frequency table provided in the assignment description
      word with highest frequency gets lower point , for example letter 'e'
"""
scoreTable = {
    'a': 3, 'b': 20, 'c': 12, 'd': 10, 'e': 1, 'f': 16, 'g': 17, 'h': 8, 'i': 5,
    'j': 23, 'k': 22, 'l': 11, 'm': 14, 'n': 6, 'o': 4, 'p': 19, 'q': 25,
    'r': 9, 's': 7, 't': 2, 'u': 13, 'v': 21, 'w': 15, 'x': 24, 'y': 18, 'z': 26
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
