class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        

        rows = len(grid)
        cols = len(grid[0])

        resCount = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.markIsland(row,col,grid)
                    resCount+=1
        return resCount

    
    def markIsland(self, row, col,grid):
        
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 
        
        if grid[row][col] == "1":
            grid[row][col] = "#"
            self.markIsland(row + 1, col,grid)
            self.markIsland(row-1, col,grid)
            self.markIsland(row,col+1,grid)
            self.markIsland(row,col-1,grid)
