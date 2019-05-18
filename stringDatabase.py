import random

file_content = open("four_letters.txt", "r")
wordList = []
words = file_content.read().split(' ')  # this word may have word like 'abc\nabk' below for loop will remove all \n
for word in words:
    if "\n" in word:
        tempWords = word.split("\n")
        for tempWord in tempWords:
            wordList.append(tempWord)
    else:
        wordList.append(word)

"""
This class is for  database of words . Class contains method to select random word 

"""


class database:
    """
       This method will get the random word from the string database .
       All words are stored in words variable defined before the class definition
    """

    def getWord(self):
        """
              return random word from the string database
              :return: random word
        """
        return random.choice(wordList)
