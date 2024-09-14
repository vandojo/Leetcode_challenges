'''descriptions

Given an m x n matrix, return all elements of the matrix in spiral order.
'''

# SOLUTION

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])

        x = 0
        y = 0
        dx = 1
        dy = 0

        output = []

        for i in range(rows * cols):
            output.append(matrix[y][x])

            matrix[y][x] = "."
            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y+dy][x+dx] == "." :
                dx, dy = -dy, dx
            
            x += dx
            y += dy
        
        return output

        