class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        # # means we have counted this island

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == "1"):
                    self.helper(grid, r, c)
                    res +=1
        return res

    def helper(self,grid,r,c):
        if 0<=r < len(grid) and 0<=c< len(grid[0]) and grid[r][c] == "1":
            grid[r][c] = "#"
            movements = [(1,0),(-1,0),(0,1), (0,-1)]
            for movex,movey in movements:
                self.helper(grid, r + movex, c + movey)
    
