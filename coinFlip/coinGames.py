import random


class gameA(object):
    def __init__(object, coinSideBetted, initialCapital, amountOfBets):
        percentageOfTails = 0.49
        executeCoinFlip(coinSideBetted, initialCapital, amountOfBets,
                        percentageOfTails, 'Game A')


class gameB(object):
    def __init__(object, coinSideBetted, initialCapital, amountOfBets):
        percentageOfTails = 0.09
        executeCoinFlip(coinSideBetted, initialCapital, amountOfBets,
                        percentageOfTails, 'Game B')


def executeCoinFlip(coinSideBetted, initialCapital, amountOfBets, percentageOfTails, gameName, secondPercentegeOfTails=0):
    print(gameName)
    finalCaptial = initialCapital
    for i in range(amountOfBets):
        print("Bet "+str(i)+" of " + str(amountOfBets))
        if ("B" in gameName):
            if (not (finalCaptial % 3 == 0)):
                percentageOfTails = 0.74
            else:
                percentageOfTails = 0.09

        result = probably(percentageOfTails)
        if (result):
            finalCaptial += 1
        else:
            finalCaptial -= 1

        textResult(result, coinSideBetted)
    if (finalCaptial < initialCapital or finalCaptial == 0):
        print("You lost money!")
    else:
        print("You won more USD"+str(finalCaptial - initialCapital))
    print("Final balance: USD"+str(finalCaptial - initialCapital))
    print("You've played "+str(amountOfBets)+" times.")
    print('End '+gameName+";")
    print('--------------------')
    print('')


def probably(chance):
    return random.random() < chance


def textResult(result, choice):
    choosenCoinSide = 'Head'
    if (choice == 't'):
        choosenCoinSide = 'Tails'
    if (result):
        print("Player wins one dollar!")
        print("Coin landed on " + choosenCoinSide)
    else:
        print("Player lost one dollar!")
        print("Coin landed on " + ('Head' if choice == 't' else 'Tails'))
    print('--------------------')
