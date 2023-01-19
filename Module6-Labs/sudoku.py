sudoku = """295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672"""

sudoku = sudoku.split()

sudokuList = [] # code block assembles sudokuList, which is a nested list containing all the values for each row. also assembles a 
rowList = [] # assembles row list.  contents of row list e.g. [2,9,5,7,4,3,8,6,1] are then joined and sorted 1-9
for i in sudoku:
    sudokuList.append(list(i))
    rowList.append("".join(sorted(list(i))))

rowMatch = True # analyses rows
for i in rowList:
    if i == "123456789":
        rowMatch = True
    else:
        rowMatch = False
        break

columnList = [] # assembles columnList
counter = 81
rowCord = 0
columnCord = 0

while counter != 0:
    columnList.append((sudokuList[rowCord][columnCord]))
    rowCord += 1
    counter -= 1
    if counter % 9 == 0:
        columnList.append(" ")
        rowCord = 0
        columnCord += 1
columnList = "".join(columnList)
columnList = (columnList.split())

newColumnList = [] # assembles new sorted newColumnList for analysis
for i in columnList:
    newColumnList.append("".join(sorted(list(i))))

columnMatch = True
for i in newColumnList:
    if i == "123456789":
        columnMatch = True
    else:
        columnMatch = False
        break

boxList = [] # assembles box list
counter = 27
rowCord = 0
columnCord = 0
while counter != 0:
    boxList.append(sudokuList[rowCord][columnCord])
    columnCord += 1
    counter -= 1
    if counter % 3 == 0:
        rowCord += 1
        columnCord = 0
    if counter % 9 == 0:
        boxList.append(" ")

counter = 27
rowCord = 0
columnCord = 3
while counter != 0:
    boxList.append(sudokuList[rowCord][columnCord])
    columnCord += 1
    counter -= 1
    if counter % 3 == 0:
        rowCord += 1
        columnCord = 3
    if counter % 9 == 0:
        boxList.append(" ")

counter = 27
rowCord = 0
columnCord = 6
while counter != 0:
    boxList.append(sudokuList[rowCord][columnCord])
    columnCord += 1
    counter -= 1
    if counter % 3 == 0:
        rowCord += 1
        columnCord = 6
    if counter % 9 == 0:
        boxList.append(" ")

boxList = "".join(boxList)
boxList = boxList.split()

newBoxList = [] # create newBoxList for analysis
for i in boxList:
    newBoxList.append("".join(sorted(list(i)))) 

boxMatch = True # analyse boxList
for i in newBoxList:
    if i == "123456789":
        boxMatch = True
    else:
        boxMatch = False
        break

if rowMatch == True and columnMatch == True and boxMatch == True: # checks all rows = 1-9, all columns = 1-9 and all 3x3 boxes = 1-9
    print("Yes")
else:
    print("No")

"""Test data

295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

Output:
Yes

195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671

Output:
No"""