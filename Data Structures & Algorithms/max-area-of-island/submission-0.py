class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        res = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    currCount = self.countIslandArea(row,col,grid)
                    res = max(res,currCount)
        return res

    def countIslandArea(self,row,col,grid):
        
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0
        if grid[row][col] == 0 or grid[row][col] == -1:
            return 0
    
        grid[row][col] = -1
        return 1 + self.countIslandArea(row+1,col,grid) \
        + self.countIslandArea(row-1,col,grid) \
        + self.countIslandArea(row,col+1,grid) \
        + self.countIslandArea(row,col-1,grid)  
        