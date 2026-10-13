class Solution:
    def solve(self, board: List[List[str]]) -> None:
         # Naive soluton
        rows = len(board)
        cols = len(board[0])
        # Prevents Loops
        visited = set()

        # Marks those that are not surrounded by X
        safeAreas = set()

        # Search Top and Bottom
        for c in range(cols):
            self.dfs(0,c,visited,safeAreas,board)
            self.dfs(rows-1,c,visited,safeAreas,board)

        # Search Left and Right
        for r in range(rows):
            self.dfs(r,0,visited,safeAreas,board)
            self.dfs(r,cols-1,visited,safeAreas,board)

        # Mark those not in safeAreas
        for row in range(rows):
            for col in range(cols):
                if (row,col) not in safeAreas:
                    board[row][col] = 'X'
        
    # -> Mark those row,col that are safe and return nothing
    def dfs(self, row, col, visited,safeAreas,board):
        
        # Assess if it's not a valid 'O'
        if row < 0 or row >= len(board):
            return
        if col < 0 or col >= len(board[0]):
            return
        if (row,col) in visited:
            return
        if board[row][col] == 'X':
            return
        
        visited.add((row,col))
        safeAreas.add((row,col))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for x,y in directions:
            self.dfs(row+x,col+y,visited,safeAreas,board)
        


    
    

