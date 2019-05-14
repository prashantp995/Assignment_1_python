import random


def main():
    file_content = open("four_letters.txt", "r");
    words = file_content.read().split(' ');

    for word in words:
        print(word)
    print("random word " + random.choice(words));
    print("enter you choice");
    choice = int(input());
    print("your choice is ");
    print(choice);


main()
