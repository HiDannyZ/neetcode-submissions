class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Search for a 1 
        # DFS to explore the whole island
        # Mark or we can mark it with a "#"
        # Modify Grid in place
        if not grid:
            return 0

        res = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.dfs(row,col,grid)
                    res+=1
        return res
    
    def dfs(self,row,col,grid):
        # Out of Bound Checking
        if row < 0 or row >= len(grid):
            return
        if col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == "#" or grid[row][col] == "0":
            return
        
        grid[row][col] = "#"

        self.dfs(row+1,col,grid)
        self.dfs(row-1,col,grid)
        self.dfs(row,col+1,grid)
        self.dfs(row,col-1,grid)


    