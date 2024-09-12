'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
'''



# Solution


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])        
        directions = [(1,0), (1,-1),(0,-1),(-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        for i in range(rows):
            for j in range(cols):
                alive = 0

                for x,y in directions:
                    if (i+x <rows and i+x >=0) and (j+y<cols and j+y>=0) and abs(board[i+x][j+y]) == 1:
                        alive += 1
            
                if board[i][j] == 1 and (alive<2 or alive > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and alive == 3:
                    board[i][j] = 2
        for i in range(rows):
            for j in range(cols):
                board[i][j] =1 if (board[i][j] > 0) else 0
        return board

