class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Input
            # No Cycles
            # Undirected graph with list of edges 
        # Output:
            # Remove the edge that causes a cycle and is last in the input of edges


        # Adjacency List of Undirected Graph
        neighbors = defaultdict(list)
        
        for v1,v2 in edges:
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)
            prev = -1

            # Find Cycle
            visited = set()
            
            if not self.dfs(v1,prev,neighbors,visited):
                return [v1,v2]
        return []
    
    def dfs(self,v1, prev,neighbors,visited):
        
        if v1 in visited:
            return False

        visited.add(v1)
        for neighbor in neighbors[v1]:
            if neighbor == prev:
                continue
            if not self.dfs(neighbor,v1,neighbors,visited):
                return False
        return True
        
