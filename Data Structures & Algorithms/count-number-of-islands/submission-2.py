class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Change the 1s to a random input like #
        # Go through the matrix by each value
        # Bottle necked by that O(n)
        # Solution here is to go through each one
        if not grid:
            return 

        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.discoverIsland(row,col,grid)
                    res +=1
        return res
    
    def discoverIsland(self,row,col,grid):
        if not (0 <= row < len(grid) and 0 <=col < len(grid[0])):
            return        
        if grid[row][col] != "1":
            return
        grid[row][col] = "#"
        movements = [(1,0),(-1,0),(0,1), (0,-1)]

        for x,y in movements:
            self.discoverIsland(row+x,col+y,grid)