def diagonalSum(matrix):
    sum = 0

    # for i in range(0, len(matrix)):
    #     for j in range(0, len(matrix[0])):
            
    #         # primary diagonal
    #         if i == j:
    #             sum += matrix[i][j]
            
    #         # secondary diagonal
    #         elif i+j == len(matrix)-1:
    #             sum += matrix[i][j]
    

    for i in range(0, len(matrix)):
        #pd
        sum += matrix[i][i]
        #sd
        if(i != len(matrix)-1-i):
            sum += matrix[i][len(matrix)-i-1]

    return sum


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


sum = diagonalSum(matrix)
print(sum)
