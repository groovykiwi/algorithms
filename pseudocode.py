linearPseudocode = '''
DECLARE list : ARRAY[0:8] OF INTEGER
DECLARE item : INTEGER
DECLARE found : BOOLEAN
DECLARE i : INTEGER

OUTPUT "Enter the item to search"
INPUT ITEM

FOR i <-- 0 TO LENGHT(list)
    IF item = list[i] THEN found <-- True
ENDFOR

IF found = True THEN 
    OUTPUT "Item is in the list"
ELSE 
    OUTPUT "Item is not in the list"
ENDIF'''


binaryPseudocode = '''
DECLARE list : ARRAY[0:8] OF INTEGER
DECLARE item : INTEGER
DECLARE found : BOOLEAN
DECLARE left : INTEGER
DECLARE right : INTEGER
DECLARE mid : INTEGER

found <-- False
left <-- 0
right <-- LENGTH(list) - 1

WHILE found = False AND left <= right DO
    mid <-- INT((left + right) / 2)
    IF list[mid] = item THEN
        found <-- True
    ELIF item > list[mid] THEN
        left <-- mid + 1
    ELIF item < list[mid] THEN
        right <-- mid - 1
ENDWHILE

IF found = True THEN 
    OUTPUT "Item is in the list"
ELSE 
    OUTPUT "Item is not in the list"
ENDIF'''

bubblePseudocode = '''
DECLARE list : ARRAY[0:8] OF INTEGER
DECLARE swap : BOOLEAN
DECLARE i : INTEGER
DECLARE temp : INTEGER

swap <-- True
WHILE swap = True DO
    swap <-- False
    FOR i <-- 0 TO LENGTH(list) - 1
        IF list[i] > list[i+1] THEN
            temp <-- list[i]
            list[i] <-- list[i+1]
            list[i+1] <-- temp
            swap <-- True
        ENDIF
    ENDFOR
ENDWHILE
OUTPUT list
'''

insertionPseudocode = '''
DECLARE list : ARRAY[0:8] OF INTEGER
DECLARE i : INTEGER
DECLARE j : INTEGER
DECLARE temp : INTEGER

FOR i <-- 1 TO LENGHT(list)
    j <-- i
    WHILE j > 0 DO
        IF list[j] < list[j-1] THEN
            temp <-- list[j]
            list[j] <-- list[j-1]
            list[j-1] <-- temp
        ENDIF
        j <-- j - 1
ENDFOR
OUTPUT list'''

queuePseudocode = '''
Not finished'''

stackPseudocode = '''
Not finished'''
