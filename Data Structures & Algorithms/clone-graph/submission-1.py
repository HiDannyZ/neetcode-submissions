"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Construct a hashmap, which contains the old node to cloned new node 
        if not node:
            return 
        oldToNew = {}
        firstNode = Node(node.val)
        oldToNew[node] = firstNode

        self.dfs(node,oldToNew)


        return firstNode

    # Actions to do:
    # Clone a node
    # Add it to the hashmap
    # peak at it's neighbors
    # Link to neighbors
    # after all neighbors are peaked, return

    def dfs(self,node, oldToNew):
        
        for neighbor in node.neighbors:
            if neighbor not in oldToNew:
                cloneNei = Node(neighbor.val)
                oldToNew[neighbor] = cloneNei
                self.dfs(neighbor,oldToNew)
            # Clone of the current Node
            cloneNode = oldToNew[node]
            # Clone of neighbor
            cloneNei = oldToNew[neighbor]
            cloneNode.neighbors.append(cloneNei)


            