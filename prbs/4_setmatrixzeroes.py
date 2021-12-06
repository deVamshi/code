# Question
# https://leetcode.com/problems/set-matrix-zeroes/
#
class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zeroIndexes = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroIndexes.append([i, j])

        for i in zeroIndexes:
            for row in range(m):
                matrix[row][i[1]] = 0

            for col in range(n):
                matrix[i[0]][col] = 0


#
class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        row_matrix = [False] * m
        col_matrix = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_matrix[i] = True
                    col_matrix[j] = True

        for i in range(m):
            for j in range(n):
                if row_matrix[i] or col_matrix[j]:
                    matrix[i][j] = 0
class Solution3:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_row_has_zero = False
        zero_col_has_zero = False

        for row  in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
                    if row == 0:
                        zero_row_has_zero = True
                    if col == 0:
                        zero_col_has_zero = True

        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if zero_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        if zero_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0
