class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n < 1:
            return True

        # Adjacency List - Keep track of all neighbors
        neighbors = defaultdict(list)
        for v1, v2 in edges:
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)
        
        # No Cycles - use a set to keep track of what we visit
        visited = set()
        
        # We need to keep track of prev as when we perform DFS, we need to not see the prev node in our visited set
        prev = -1
        if not self.dfs(0,prev,n,neighbors,visited):
            return False
        return len(visited) == n


    
    def dfs(self, vertice, prev, n, neighbors,visited):
        # Check if in visited
        if vertice in visited:
            return False
        visited.add(vertice)
        # Check neighbors are connected
        for newVertice in neighbors[vertice]:
            if newVertice == prev:
                continue
            if not self.dfs(newVertice,vertice, n,neighbors,visited):
                return False
        return True
