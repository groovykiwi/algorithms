import os
import inspect as i
from simple_term_menu import TerminalMenu
from pseudocode import *
from pyalgorithms import *

# Colors
reset = '\033[0m'
bold = '\033[01m'
disable = '\033[02m'
underline = '\033[04m'
red = '\033[31m'


def intCheck(value):
    try:
        value = int(value)
        return value
    except:
        print(f"\n{red}Input is not an integer{reset}")
        return False


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


# Menus


def mainMenu():
    clear()
    print(f"{bold}{underline}Select a search algorithm{reset}")
    searchMenu = TerminalMenu(["Linear", "Binary", "Exit script"])
    searchMenuEntryIndex = searchMenu.show()
    if(searchMenuEntryIndex) == 0:
        linearMenu()
    elif(searchMenuEntryIndex) == 1:
        binaryMenu()
    elif(searchMenuEntryIndex) == 2:
        clear()
        exit()


def linearMenu():
    clear()
    print(f"{bold}{underline}Linear Search{reset}")
    linearMenu = TerminalMenu(
        ["Run a test example", "Display the python code", "Display the pseudocode", "Go back "])
    linearMenuEntryIndex = linearMenu.show()
    if(linearMenuEntryIndex) == 0:
        linear(ary)
        input(f"{disable}\nPress ENTER to go back {reset}")
        linearMenuBack()
    elif(linearMenuEntryIndex) == 1:
        print(linearPython)
        input(f"{disable}\nPress ENTER to go back {reset}")
        linearMenuBack()
    elif(linearMenuEntryIndex) == 2:
        print(linearPseudocode)
        input(f"{disable}\nPress ENTER to go back {reset}")
        linearMenuBack()
    elif(linearMenuEntryIndex) == 3:
        mainMenu()


def linearMenuBack():
    linearMenu()


def binaryMenu():
    clear()
    print(f"{bold}{underline}Binary Search{reset}")
    binaryMenu = TerminalMenu(
        ["Run a test example", "Display the python code", "Display the pseudocode", "Go back "])
    binaryMenuEntryIndex = binaryMenu.show()
    if(binaryMenuEntryIndex) == 0:
        binary(ary)
        input(f"{disable}\nPress ENTER to go back {reset}")
        binaryMenuBack()
    elif(binaryMenuEntryIndex) == 1:
        print(binaryPython)
        input(f"{disable}\nPress ENTER to go back {reset}")
        binaryMenuBack()
    elif(binaryMenuEntryIndex) == 2:
        print(binaryPseudocode)
        input(f"{disable}\nPress ENTER to go back {reset}")
        binaryMenuBack()
    elif(binaryMenuEntryIndex) == 3:
        mainMenu()


def binaryMenuBack():
    binaryMenu()


def clear():
    # Should remove nt check as only works on posix
    os.system('cls' if os.name == 'nt' else 'clear')


ary = [3, 8, 14, 27, 45, 68, 79, 98]
mainMenu()
