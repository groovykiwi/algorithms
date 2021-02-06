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
print("Example list:", list)
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
