'''

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.'''

# Solution

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])

        row = [False] * rows
        col = [False] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        
        for i in range(rows):
            for j in range(cols):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        return matrix