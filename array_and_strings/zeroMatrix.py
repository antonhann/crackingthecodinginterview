import check as check
def fillRow(rowIndex,matrix):
    for j in range(len(matrix[0])):
        matrix[rowIndex][j] = 0

def fillCol(colIndex, matrix):
    for i in range(len(matrix)):
        matrix[i][colIndex] = 0

def zeroMatrix(matrix):
    fillIn = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                fillIn.append([i,j])
    for i, j in fillIn:
        fillRow(i,matrix)
        fillCol(j,matrix)
    return matrix

testcase = [
    [[1,2,3],
    [4,0,6],
    [7,8,9]]
]

shouldBe = [
    [[1,0,3],
     [0,0,0],
     [7,0,9]]
]

check.checkOneParam(testcase,shouldBe,zeroMatrix)
