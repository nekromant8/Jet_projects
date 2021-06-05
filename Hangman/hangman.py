import random

print("H A N G M A N")


def game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    correct = random.choice(word_list)
    entered = set()
    hidden = "-" * len(correct)
    list_hidden = list(hidden)
    error = 0
    while error != 8:
        print()
        count = 0
        print(hidden)
        letter = input("Input a letter: ")
        num = correct.count(letter)
        if letter in entered:
            print("You've already guessed this letter")
            continue
        elif len(letter) != 1:
            print("You should input a single letter")
            continue
        elif not letter.isalpha() or letter.isupper():
            print("Please enter a lowercase English letter")
            continue
        if letter in hidden:
            print("No improvements")
            error = error + 1
        elif letter in correct:
            for i in range(0, num):
                ind = correct.find(letter, count, len(correct))
                list_hidden[ind] = letter
                count = ind + 1
            hidden = "".join(list_hidden)
        else:
            error = error + 1
            print("That letter doesn't appear in the word")
        entered.add(letter)
        if hidden == correct:
            break
    if hidden == correct:
        print("You guessed the word " + hidden + "!")
        print("You survived!")
        menu()
    else:
        print("You lost!")
        menu()


def menu():
    user_input = None
    while user_input != "play" or user_input != "exit":
        user_input = input('Type "play" to play the game, "exit" to quit: ')
        if user_input == "play":
            game()
        elif user_input == "exit":
            exit()


menu()
