import os

from simple_term_menu import TerminalMenu
from pseudocode import *
from pyalgorithms import *

# Colors
nt = '\033[0m'
bt = '\033[01m'
dt = '\033[02m'
ut = '\033[04m'
red = '\033[31m'
yel = '\033[33m'
blu = '\033[34m'


# Quality of life
def intCheck(value):
    try:
        value = int(value)
        return value
    except:
        print(f"\n{red}Input is not an integer{nt}")
        return False


def clear():
    # Should remove nt check as only works on posix
    os.system('clear')


# Search Algorithms
def linear(list):

    print("Example list:", list)
    item = input("Enter the item to search: ")
    if intCheck(item) == False:
        return
    else:
        item = intCheck(item)

    found = False
    for i in range(len(list)):
        print(i, 'check:', list[i], '=', item)
        if list[i] == item:
            found = True
            break

    if found == True:
        print("Item is in the list")
    elif found == False:
        print("Item is not in the list")


def binary(list):
    print("Example list:", list)
    item = input("Enter the item to search: ")
    if intCheck(item) == False:
        return
    else:
        item = intCheck(item)

    found = False
    left = 0
    right = len(list) - 1

    while found == False and left <= right:
        mid = int((left+right)/2)
        print('left:', left, '| right:', right, '| mid:',
              mid, '| mid value:', list[mid], '| item:', item)
        if item == list[mid]:
            found = True
        elif item > list[mid]:
            left = mid + 1
        elif item < list[mid]:
            right = mid - 1

    if found == True:
        print("Item is in the list")
    elif found == False:
        print("Item is not in the list")


# Sorting Algorithms
def bubble(list):
    print("\nOriginal list:", list, "\n")
    swap = True
    while swap == True:
        swap = False
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swap = True
        if swap == False:
            print("\nSorted list:", list)
        else:
            print(list)


def insertion(list):
    print("\nOriginal list:", list, "\n")
    for i in range(1, len(list)):
        j = i
        print(f"Sorting from index {blu}{bt}{i}{nt} and below")
        while j > 0:
            if list[j] < list[j-1]:

                clist = []
                for a in list:
                    clist.append(a)
                clist[j] = f"{red}{clist[j]}{nt}"
                clist[j-1] = f"{yel}{clist[j-1]}{nt}"
                print("[", end='')
                for b in range(len(clist) - 1):
                    print(f"{clist[b]}, ", end='')
                print(f"{clist[len(list)-1]}]")

                list[j], list[j-1] = list[j-1], list[j]
            j -= 1
            print(list)
        print("")
    print("Sorted list:", list)


# Data Strutures
queueAry = [None, None, None, None, None]
qlength = 0
qfull = 5
qfirst = 0
qlast = -1


def queue():
    clear()
    global queueAry, qlength, qfull, qlast, qfirst

    def push():
        global queueAry, qlength, qlast
        value = input("\nEnter a value to push to the queue: ")
        if qlength == qfull:
            print("Queue is full.")
            input(f"{dt}\nPress ENTER to continue {nt}")
        else:
            if qlast == qfull - 1:
                qlast = 0
            else:
                qlast += 1
            queueAry[qlast] = value
            qlength += 1
        queue()

    def pop():
        global queueAry, qlength, qfirst
        if qlength == 0:
            print("\nQueue is empty.")
            input(f"{dt}\nPress ENTER to continue {nt}")
        else:
            item = queueAry[qfirst]
            queueAry[qfirst] = None
            qlength -= 1
            if qfirst == qfull - 1:
                qfirst = 0
            else:
                qfirst += 1
            print(f"\n{red}{item}{nt} will be popped")
            input(f"{dt}\nPress ENTER to continue {nt}")
        queue()

    print(f"Status: {queueAry}")
    menu = TerminalMenu(["Push a value", "Pop", "Go back"])
    menuIndex = menu.show()
    if menuIndex == 0:
        push()
    elif menuIndex == 1:
        pop()
    elif menuIndex == 2:
        queueMenu()


stackAry = [None, None, None, None, None]
slength = 0
sfull = 5
sbase = 0
stop = -1


def stack():
    clear()
    global stackAry, slength, sfull, sbase, stop

    def push():
        global stackAry, slength, stop
        value = input("\nEnter a value to push to the queue: ")
        if slength == sfull:
            print("Stack is full.")
            input(f"{dt}\nPress ENTER to continue {nt}")
        else:
            stop += 1
            slength += 1
            stackAry[stop] = value
        stack()

    def pop():
        global stackAry, slength, stop
        if slength == 0:
            print("\nStack is empty.")
            input(f"{dt}\nPress ENTER to continue {nt}")
        else:
            item = stackAry[stop]
            stackAry[stop] = None
            stop -= 1
            slength -= 1
            print(f"\n{red}{item}{nt} will be popped")
            input(f"{dt}\nPress ENTER to continue {nt}")
        stack()

    print(f"Status: {stackAry}")
    menu = TerminalMenu(["Push a value", "Pop", "Go back"])
    menuIndex = menu.show()
    if menuIndex == 0:
        push()
    elif menuIndex == 1:
        pop()
    elif menuIndex == 2:
        stackMenu()
# Menus


def mainMenu():
    clear()
    print(f"{bt}{ut}Computer Science A Level Programming{nt}")
    menu = TerminalMenu(
        ["Sorting algorithms", "Search algorithm", "Data Structures", "Exit script"])
    menuIndex = menu.show()
    if(menuIndex) == 0:
        sortMenu()
    elif(menuIndex) == 1:
        searchMenu()
    elif(menuIndex) == 2:
        dataMenu()
    elif(menuIndex) == 3:
        clear()
        exit()


def searchMenu():
    clear()
    print(f"{bt}{ut}Select a search algorithm{nt}")
    menu = TerminalMenu(["Linear", "Binary", "Go back"])
    menuIndex = menu.show()
    if(menuIndex) == 0:
        linearMenu()
    elif(menuIndex) == 1:
        binaryMenu()
    elif(menuIndex) == 2:
        clear()
        mainMenu()


def sortMenu():
    clear()
    print(f"{bt}{ut}Select a search algorithm{nt}")
    menu = TerminalMenu(["Bubble", "Insertion", "Go back"])
    menuIndex = menu.show()
    if(menuIndex) == 0:
        bubbleMenu()
    elif(menuIndex) == 1:
        insertionMenu()
    elif(menuIndex) == 2:
        clear()
        mainMenu()


def dataMenu():
    clear()
    print(f"{bt}{ut}Select a data structure{nt}")
    menu = TerminalMenu(["Queue", "Stack", "Go back"])
    menuIndex = menu.show()
    if(menuIndex) == 0:
        queueMenu()
    elif(menuIndex) == 1:
        stackMenu()
    elif(menuIndex) == 2:
        clear()
        mainMenu()


def linearMenu():
    clear()
    print(f"{bt}{ut}Linear Search{nt}")
    menu = TerminalMenu(
        ["Run a test example", "Display the python code", "Display the pseudocode", "Go back "])
    menuIndex = menu.show()
    if(menuIndex) == 0:
        linear(searchList)
        input(f"{dt}\nPress ENTER to go back {nt}")
        linearMenu()
    elif(menuIndex) == 1:
        print(linearPython)
        input(f"{dt}\nPress ENTER to go back {nt}")
        linearMenu()
    elif(menuIndex) == 2:
        print(linearPseudocode)
        input(f"{dt}\nPress ENTER to go back {nt}")
        linearMenu()
    elif(menuIndex) == 3:
        searchMenu()


def binaryMenu():
    clear()
    print(f"{bt}{ut}Binary Search{nt}")
    menu = TerminalMenu(
        ["Run a test example", "Display the python code", "Display the pseudocode", "Go back "])
    menuIndex = menu.show()
    if(menuIndex) == 0:
        binary(searchList)
        input(f"{dt}\nPress ENTER to go back {nt}")
        binaryMenu()
    elif(menuIndex) == 1:
        print(binaryPython)
        input(f"{dt}\nPress ENTER to go back {nt}")
        binaryMenu()
    elif(menuIndex) == 2:
        print(binaryPseudocode)
        input(f"{dt}\nPress ENTER to go back {nt}")
        binaryMenu()
    elif(menuIndex) == 3:
        searchMenu()


def bubbleMenu():
    clear()
    print(f"{bt}{ut}Bubble Sort{nt}")
    menu = TerminalMenu(
        ["Run a test example", "Display the python code", "Display the pseudocode", "Go back "])
    menuIndex = menu.show()
    if(menuIndex) == 0:
        bubble(sortList)
        input(f"{dt}\nPress ENTER to go back {nt}")
        bubbleMenu()
    elif(menuIndex) == 1:
        print(bubblePython)
        input(f"{dt}\nPress ENTER to go back {nt}")
        bubbleMenu()
    elif(menuIndex) == 2:
        print(bubblePseudocode)
        input(f"{dt}\nPress ENTER to go back {nt}")
        bubbleMenu()
    elif(menuIndex) == 3:
        sortMenu()


def insertionMenu():
    clear()
    print(f"{bt}{ut}Insertion Sort{nt}")
    menu = TerminalMenu(
        ["Run a test example", "Display the python code", "Display the pseudocode", "Go back "])
    menuIndex = menu.show()
    if(menuIndex) == 0:
        insertion(sortList)
        input(f"{dt}\nPress ENTER to go back {nt}")
        insertionMenu()
    elif(menuIndex) == 1:
        print(insertionPython)
        input(f"{dt}\nPress ENTER to go back {nt}")
        insertionMenu()
    elif(menuIndex) == 2:
        print(insertionPseudocode)
        input(f"{dt}\nPress ENTER to go back {nt}")
        insertionMenu()
    elif(menuIndex) == 3:
        sortMenu()


def queueMenu():
    clear()
    print(f"{bt}{ut}Queue (FIFO/LILO){nt}")
    menu = TerminalMenu(
        ["Run a test example", "Display the python code", "Display the pseudocode", "Go back "])
    menuIndex = menu.show()
    if(menuIndex) == 0:
        queue()
        input(f"{dt}\nPress ENTER to go back {nt}")
        queueMenu()
    elif(menuIndex) == 1:
        print(queuePython)
        input(f"{dt}\nPress ENTER to go back {nt}")
        queueMenu()
    elif(menuIndex) == 2:
        print(queuePseudocode)
        input(f"{dt}\nPress ENTER to go back {nt}")
        queueMenu()
    elif(menuIndex) == 3:
        dataMenu()


def stackMenu():
    clear()
    print(f"{bt}{ut}Stack (FILO/LIFO){nt}")
    menu = TerminalMenu(
        ["Run a test example", "Display the python code", "Display the pseudocode", "Go back "])
    menuIndex = menu.show()
    if(menuIndex) == 0:
        stack()
        input(f"{dt}\nPress ENTER to go back {nt}")
        stackMenu()
    elif(menuIndex) == 1:
        print(stackPython)
        input(f"{dt}\nPress ENTER to go back {nt}")
        stackMenu()
    elif(menuIndex) == 2:
        print(stackPseudocode)
        input(f"{dt}\nPress ENTER to go back {nt}")
        stackMenu()
    elif(menuIndex) == 3:
        dataMenu()


searchList = [3, 8, 14, 27, 45, 68, 79, 98]
sortList = [36, 12, 22, 44, 8, 45]

mainMenu()
clear()
