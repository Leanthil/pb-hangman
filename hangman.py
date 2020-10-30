import random


def menu():
    print("\033c")
    print(""" _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |
                   |___/
        Hi! Welcome to the Hangman game!
             1: Easy        2: Hard""")
    difficulty = int(input("      Please choose a difficulty! (1/2): "))
    play(readfile(difficulty), lifecount(difficulty))


def lifecount(easyorhard):
    if easyorhard == 1:
        return 9
    else:
        return 7


def readfile(easyorhard):
    if easyorhard == 1:
        diff = 0
    else:
        diff = 1
    hidden = ''
    file1 = open('countries-and-capitals.txt', 'r')
    countryandcapital = file1.readlines()
    file1.close()
    number = random.randint(0, len(countryandcapital))
    hidden = countryandcapital[number].split(' | ')[diff]
    return hidden


def play(word, lives):
    print("\033c")
    guesses = {''}
    print('_ ' * len(word))
    print(hangman(lives))
    while lives != 0:
        missing = 0
        print('Your previous guesses:', ' '.join(guesses))
        print('Lives remaining: ', lives)
        print('If you would like to quit, type "quit"')
        guess = str(input('Enter a letter! '))
        print("\033c")
        if guess.isalpha() is False:
            print('_ ' * len(word))
            print(hangman(lives))
            print("This is not a letter!")
            continue
        if guess == 'quit':
            print("Goodbye!")
            exit()
        if guess.casefold() in guesses or guess.casefold() not in word.lower():
            if guess.casefold() not in word.lower() and guess.casefold() not in guesses:
                lives = lives - 1
            if guess in guesses:
                print("You have already guessed this letter! Try something else!")
        guesses.add(guess.lower())
        for char in word:
            if char.casefold() in guesses or not char.isalpha():
                print(char, end=' ')
            else:
                print('_', end=' ')
                missing = missing + 1
        print('\n')
        print(hangman(lives))
        if lives == 0:
            print("You lost!")
            print("The word was: " + word)
            again = str(input('Would you like to play again? (Y/N): '))
            if again == 'Y' or again == 'y':
                menu()
            else:
                print('Goodbye!')
                break
        if missing == 0:
            print("You won!")
            again = str(input('Would you like to play again? (Y/N): '))
            if again == 'Y' or again == 'y':
                menu()
            else:
                print('Goodbye!')
                break


def hangman(lives):
    stages = ['''
          +----+
          |   \\|
          O    |
         /|\\   |
         / \\   |
               |
        ==========''', '''
          +----+
          |   \\|
          O    |
         /|\\   |
         /     |
               |
        ==========''', '''
          +----+
          |   \\|
          O    |
         /|\\   |
               |
               |
        ==========''', '''
          +----+
          |   \\|
          O    |
         /|    |
               |
               |
        =========''', '''
          +----+
          |   \\|
          O    |
          |    |
               |
               |
        ==========''', '''
          +----+
          |   \\|
          O    |
               |
               |
               |
        ==========''', '''
          +----+
          |   \\|
               |
               |
               |
               |
        ==========''', '''
               |
               |
               |
               |
               |
        ==========''', '''
        ==========''', '''
                  ''']
    return stages[lives]


menu()
