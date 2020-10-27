import random


def menu():
    print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    

        Hi! Welcome to the Hangman's game!  

            1: Easy        2: Hard""")
    difficulty = int(input("       Please choose a difficulty (1/2): "))
    return difficulty


def readfile():
    if menu() == 1:
        diff = 0
    if menu() == 2:
        diff = 1
    hidden = ''
    file1 = open('countries-and-capitals.txt', 'r')
    countryandcapital = file1.readlines()
    file1.close()
    number = random.randint(0, len(countryandcapital))
    hidden = countryandcapital[number].split(' | ')[diff]
    return hidden


def play(word, lives):
    guesses = {''}
    while lives != 0:
        missing = 0
        print('Your previous guesses:', ' '.join(guesses))
        print('Lives remaining: ', lives)
        guess = input('Enter a letter: ')
        guesses.add(guess.lower())
        if guess not in word:
            lives = lives - 1
        for char in word:
            if char.casefold() in guesses or not char.isalpha():
                print(char, end=' ')
            else:
                print('_', end=' ')
                missing = missing + 1
        print('\n')
        if lives == 0:
            print("You lost!")
            break
        if missing == 0:
            print("You win!")
            break


play(readfile(), 6)
