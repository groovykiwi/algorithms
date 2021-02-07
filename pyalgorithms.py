linearPython = '''
item = int(input("Enter the item to search: "))
found = False
for i in range(len(list)):
    print(i, 'check:', list[i], '=', item)
    if list[i] == item:
        found = True
        break

if found == True:
    print("Item is in the list")
elif found == False:
    print("Item is not in the list")'''

binaryPython = '''
item = int(input("Enter the item to search: "))
found = False
left = 0
right = len(list) - 1

while found == False and left <= right:
    mid = int((left+right)/2)
    print('left:', left, '| right:', right, '| mid:',
          mid, '| mid value:', list[mid], '| item:', item)
    if list[mid] == item:
        found = True
    elif item > list[mid]:
        left = mid + 1
    elif item < list[mid]:
        right = mid - 1

if found == True:
    print("Item is in the list")
elif found == False:
    print("Item is not in the list")'''

bubblePython = '''
def bubble(list):
    swap = True
    while swap == True:
        swap = False
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swap = True
    print(list)'''

insertionPython = '''
def insertion(list):
    for i in range(1, len(list)):
        j = i
        while j > 0:
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
            j -= 1
    print(list)'''

queuePython = '''
queue = [None, None, None, None, None]
lenght = 0
full = 5
first = 0
last = -1

def push(item):
    global lenght, last
    if lenght == full:
        print("Queue is full.")
    else:
        if last == full - 1:
            last = 0
        else:
            last += 1
        queue[last] = item
        lenght += 1

def pop():
    global lenght, first
    if lenght == 0:
        print("Queue is empty.")

    else:
        item = queue[first]
        queue[first] = None
        lenght -= 1
        if first == full - 1:
            first = 0
        else:
            first += 1
        return item'''

stackPython = '''
To do
'''
