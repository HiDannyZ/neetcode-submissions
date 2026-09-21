class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Graph Problem: DFS
        # Look for the 1s
        # Count all the 1s via DFS
        # Mark the island as "#" for each space to signal completed
        # Take the max result
    

        res = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    curCount = self.dfs(row,col,grid)
                    res = max(res,curCount)
        return res

        
    def dfs(self,row,col,grid):
        if row < 0 or row >= len(grid):
            return 0
        if col < 0 or col >= len(grid[0]):
            return 0
        if grid[row][col] == 0 or grid[row][col] == -1:
            return 0
        grid[row][col] = -1
        res = 1 + self.dfs(row+1,col,grid) + self.dfs(row-1,col,grid) + self.dfs(row,col+1,grid) + self.dfs(row,col-1,grid)
        return res