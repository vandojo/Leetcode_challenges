'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.'''


# Solution

class Solution:
    def breadth_first(self, r, c, grid):
        q = deque()
        self.checked.add((r,c))
        q.append((r,c))

        while q:
            row, col = q.popleft()
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr, dc in dirs:
                r = row + dr
                c = col + dc

                if 0 <= r < self.rows and 0 <= c < self.cols and grid[r][c] == "1" and (r, c) not in self.checked:
                        q.append((r, c))
                        self.checked.add((r, c)) 
                
    def numIslands(self, grid: List[List[str]]) -> int:

        self.rows = len(grid)
        self.cols = len(grid[0])
        ans = 0
        self.checked = set()

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == "1" and (r,c) not in self.checked:
                    ans += 1
                    self.breadth_first(r,c,grid)
        
        return ans



        