import random


def readfile():
    hidden = ''
    file1 = open('countries-and-capitals.txt', 'r')
    countryandcapital = file1.readlines()
    file1.close()
    number = random.randint(0, len(countryandcapital))
    hidden = countryandcapital[number].split(' | ')[0]
    return hidden


def play(word, lives):
    guesses = {'a', 'r'}
    while lives > 0:
        missing = 0
        guess = input('Enter a letter:')
        guesses.add(guess.lower())
        for char in word:
            if char.casefold() in guesses or not char.isalpha():
                print(char, end=' ')
            else:
                print('_', end=' ')
                missing = missing + 1
        print('\n')
        if missing == 0:
            print("A winner is you!")
            break


play('Saudi Arabia', 6)
