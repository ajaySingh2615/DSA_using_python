def printSpiral(list1):
    startRow = 0
    startCol = 0
    endRow = len(list1)-1
    endCol = len(list1[0])-1

    while startRow <= endRow and startCol <= endCol:

        #top boundary (j=col, i=row)
        for j in range(startCol, endCol+1):
            print(list1[startRow][j], end=" ")
        
        #right boundary
        for i in range(startRow+1, endRow+1):
            print(list1[i][endCol], end=" ")

        # bottom boundary
        for j in range(endCol-1, startCol-1, -1):
            if startRow == endRow:
                break
            print(list1[endRow][j], end=" ")
        
        # left boundary
        for i in range(endRow-1, startRow, -1):
            if startCol == endCol:
                break
            print(list1[i][startCol], end=" ")
        
        startCol+=1;
        startRow+=1;
        endCol-=1;
        endRow-=1;
    
    print()

list1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

printSpiral(list1)

