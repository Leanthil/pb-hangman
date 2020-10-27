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


def menu():
    print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
        1: Easy     2: Medium   3: Hard
        Hi! Welcome to the Hangman's game!""")
    difficulty = int(input("Please choose a difficulty(1/2/3): "))
    play(readfile(), difficulty)


menu()
