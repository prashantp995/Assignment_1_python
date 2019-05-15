import random

file_content = open("four_letters.txt", "r");
words = file_content.read().split(' ');


class database:

    def getWord(self):
        return random.choice(words);
