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
        visited = set()
        dist = 0
        queue = deque()
        queue.append((row,col))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            queueLen = len(queue)
            for _ in range(queueLen):
                r,c = queue.popleft()
                # Check if it's a valid cell
                if r < 0 or r >= len(grid):
                    continue
                if c < 0 or c >= len(grid[0]):
                    continue
                if (r,c) in visited:
                    continue
                if grid[r][c] == -1:
                    continue
                if grid[r][c] < dist:
                    continue
                visited.add((r,c)) 
                grid[r][c] = dist
                for x,y in directions:
                    queue.append((r+x,c+y))
            dist +=1


