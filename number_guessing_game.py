from os import name
import random
import time

number = random.randint(1, 200)

def intro():
    print("May I ask you for your name?")
    name = input()
    print(name + ", we are going to play a game." "\nI am thinking of a number between 1 and 200\n")
    time.sleep(.5)
    print("Go ahead." "\nGuess!\n")

def pick():
    guessesTaken = 0
    while guessesTaken < 10:
        time.sleep(.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)

            if guess <= 200 and guess >= 1:
                guessesTaken = guessesTaken + 1
                if guessesTaken < 10:
                    if guess < number:
                        print("The guess of the number that you have entered is" "\ntoo low\n")
                    if guess > number:
                        print("The guess of the number that you have entered is" "\ntoo high\n")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                if guess == number:
                    print("correct choice")
                    break
            if guess > 200 or guess < 1:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")

        except:
            print("I don't think that " + enter + " is a number. Sorry")

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))

playagain = "yes"
while playagain == "yes" or playagain == "y" or playagain == "Yes" or playagain == "Y" :
    intro()
    pick()
    print("Do you want to play again?")
    playagain = input()