__author__ = "Lyle Martin"

import random

NUMBERS_PER_LINE = 6

def main():
    choice = int(input('How many quick picks? '))
    for pick in range(0, choice):
        qPick = randomNumberGen()
        for num in qPick:
            print("{0:3d}".format(num), end="")

def randomNumberGen():
    qPick = []
    for number in range(NUMBERS_PER_LINE):
        randNum = random.randrange(0, 45)
        while randNum in qPick:
            randNum = random.randrange(0, 45)

        qPick.append(randNum)

    qPick.sort()
    return qPick

main()
