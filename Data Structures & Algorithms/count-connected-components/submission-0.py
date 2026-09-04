class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Adjacency Graph to Find neighbors
        neighbors = defaultdict(list)

        for v1,v2 in edges:
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)
        
        # Keep Track of what we seen
        visited = set()

        res = 0

        for vertice in range(n):
            if vertice in visited:
                continue
            self.dfs(vertice,visited,neighbors)
            res +=1
        return res    
    
    def dfs(self,vertice,visited,neighbors):

        if vertice in visited:
            return
        
        visited.add(vertice)

        for neighbor in neighbors[vertice]:
            self.dfs(neighbor,visited,neighbors)
        return 