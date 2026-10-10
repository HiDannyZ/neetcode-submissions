class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Naive Solution: DFS on each cell
            # Problematic and super slow.
        # Better Solution?
            # Starting on the border cells
            # Border cells we know are already connect
            # Pseudocode
                # Perform DFS only on the borders
                # Have a set that stores all those that Pacific can reach
                # Have a set that stores all those that Alantic can reach
                # Check if they're in both sets and then added them into result
                    # Conditions:

            
            # TC: O(n * m) -- Only exporing each cell twice in the same pass
            # SC: O(n) + O(m)

        res = []
        if not heights:
            return res

        pac, atl = set(), set()
        rows = len(heights)
        cols = len(heights[0])

        for c in range(cols):
            self.dfs(0,c,pac,heights[0][c],heights)
            self.dfs(rows-1,c,atl,heights[rows-1][c],heights)

        for r in range(rows):
            self.dfs(r,0,pac,heights[r][0],heights)
            self.dfs(r,cols-1,atl,heights[r][cols-1],heights)


        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

        

    def dfs(self,row,col,visited,prevHeight, heights):
        
        if (row,col) in visited or row >= len(heights) or row < 0 or col >= len(heights[0]) or col < 0 or col > len(heights[0]) or prevHeight > heights[row][col]:
            return
        visited.add((row,col))
        
        newHeight = heights[row][col]
        self.dfs(row+1,col,visited,newHeight,heights)
        self.dfs(row-1,col,visited,newHeight,heights)
        self.dfs(row,col-1,visited,newHeight,heights)
        self.dfs(row,col+1,visited,newHeight,heights)
                
        