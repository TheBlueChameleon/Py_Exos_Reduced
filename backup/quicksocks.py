#!/usr/bin/python3

# Code bereitgestellt von Nils Meyer. Danke hierfür.
# Siehe auch: https://xkcd.com/356/

import random

def makeSocksList(n) :
    # create n pairs of socks

    reVal = []
    for i in range(n) :
        reVal += [chr(i + 65), chr(i + 65)]

    random.shuffle(reVal)
    return reVal

def displayList(l):
    for i in range(len(l)):
        element = l[i]
        print(f'{element:2}', end="  ")
    print()

def partition(socksList, indexList, low, high):
    # in place rearrangement
    i = (low-1)                     # index of first sock
    pivotSock = socksList[high]     # pivotSock, pick the last sock for simplicity

    for j in range(low, high):
        if socksList[j] < pivotSock:
            i = i+1
            socksList[i], socksList[j] = socksList[j], socksList[i]
            indexList[i], indexList[j] = indexList[j], indexList[i]

    socksList[i+1], socksList[high] = socksList[high], socksList[i+1]
    indexList[i+1], indexList[high] = indexList[high], indexList[i+1]
    return (i+1)

def quickSocks(socksList, indexList, low, high, displayProgress):
    # unstable socks sorting matches the socks problem if socks are the same
    # for each foot by design
    if len(socksList) == 1:
        return

    # check if already sorted
    sorted = True
    for i in range(low, high):
        if socksList[i] != socksList[i+1]:
            sorted = False
            break
    if sorted == True:
        return

    if displayProgress:
        print('Progress sorting socks')
        displayList(socksList)
        displayList(indexList)

    # not sorted
    if low < high:
        pi = partition(socksList, indexList, low, high)

        quickSocks(socksList, indexList, low, pi-1, displayProgress)
        quickSocks(socksList, indexList, pi+1, high, displayProgress)

# main

nSocks = 8
displayProgress = True

socksList = makeSocksList(nSocks)
indexList = [i for i in range(2 * nSocks)]

print('Before:')
displayList(socksList)
displayList(indexList)

quickSocks(socksList, indexList, 0, 2 * nSocks - 1, displayProgress)
print('After:')
displayList(socksList)
displayList(indexList)
