'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.'''


# Solution

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        topRow = 0
        bottomRow = n - 1

        # flip top and bottom rows
        while topRow < bottomRow:

            for col in range(n):
                temp = matrix[topRow][col]
                matrix[topRow][col] = matrix[bottomRow][col]
                matrix[bottomRow][col] = temp
            topRow += 1
            bottomRow -= 1

        # flip values diagonally
        for row in range(n):
            for col in range(row+1, n):

                temp = matrix[row][col]
                matrix[row][col]= matrix[col][row]
                matrix[col][row] = temp

        return matrix