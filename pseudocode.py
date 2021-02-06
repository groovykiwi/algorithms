linearPseudocode = '''
DECLARE list : ARRAY[0:8] OF INTEGER
DECLARE item : INTEGER
DECLARE found : BOOLEAN
DECLARE i : INTEGER

OUTPUT "Enter the item to search"
INPUT ITEM

FOR i <-- 0 TO LENGHT(X)
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
