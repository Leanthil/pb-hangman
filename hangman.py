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
    difficulty = int(input("Please choose a difficulty! (1/2): "))
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
    guesses = {''}
    while lives != 0:
        missing = 0
        print('Your previous guesses:', ' '.join(guesses))
        print('Lives remaining: ', lives)
        guess = input('Enter a letter! If you would like to quit, type "quit": ')
        if guess == 'quit':
            print("Goodbye!")
            exit()
        if guess in guesses or guess not in word.lower():
            if guess not in word.lower() and guess not in guesses:
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
        if lives == 0:
            print("You lost!")
            break
        if missing == 0:
            print("You win!")
            break


menu()
