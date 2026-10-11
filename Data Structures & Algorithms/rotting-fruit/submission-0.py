
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Naive thoughts:
            # BFS
            # We have to determine all the positions with rotten fruit for each round
            # Find all locations of rotten fruits. Add them into a queue
            # If there's any neighbors to the rotten fruits, add them to queue
        
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        freshFruit = set()

        # Find all rotten fruit
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    freshFruit.add((row,col))
        
        # Start each minute
        countMin = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        firstRound = False
        while queue:
            queueLen = len(queue)
            rotten = False
            for _ in range(queueLen):
                
                rottenFruit = queue.popleft()
                r,c = rottenFruit


                # Find those that not Valid Cell
                    # Those that are freshFruit
                    # Those are in bounds
                if r < 0 or r >= rows:
                    continue
                if c < 0 or c >= cols:
                    continue
                if grid[r][c] != 1 and firstRound:
                    continue
                if grid[r][c] == 1:
                    freshFruit.remove((r,c))
                    rotten = True
                # Avoid looping
                grid[r][c] = 2
            
                # Check for other fruits to infect if there's any
                for x,y in directions:
                    queue.append((r+x,c +y))
            firstRound = True
            if rotten:
                countMin +=1

        if freshFruit:
            return -1

        return countMin


    
        

