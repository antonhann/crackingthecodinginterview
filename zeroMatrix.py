def fillRow(rowIndex,matrix):
    for j in range(len(matrix[0])):
        matrix[rowIndex][j] = 0

def fillCol(colIndex, matrix):
    for i in range(len(matrix)):
        matrix[i][colIndex] = 0

def zeroMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                fillCol(j)
                fillRow(i)
    return matrix