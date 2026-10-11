class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Naive solution: 
            # BFS solution:
                # Psuedocode:
                    # Start at treasure chests and perform BFS
                    # If ever encounter a value that's -1, 0, or inf or something that is less than our current distance, don't put into queue
                    # otherwise, put in the current distance value
                # TC: O(n * m)
                # SC: O(1)
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    self.bfs(row,col,grid)
        

    def bfs(self,row,col,grid):
        queue = deque()
        queue.append((row, col, 0))
        visited = set()
        while queue: 
            r, c, dist = queue.popleft()
            if (r, c) in visited: 
                continue
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue 
            if grid[r][c] == -1:  
                continue 
            elif row != r and col != c and grid[r][c] == 0:
                continue
            elif grid[r][c] < dist: 
                continue 
            grid[r][c] = dist 
            queue.append((r+1, c, dist+1))
            queue.append((r, c+1, dist+1))
            queue.append((r-1, c, dist+1))
            queue.append((r, c-1, dist+1))
            visited.add((r, c))

        

