"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Old Node : New Version of Node
        # Approach
        # Create New Version of Node before adding it to neighbors
        # Do it as a dfs
        # Create new Version of node if it doesn't exist
        # After that, Check its neighbors and repeat if it doesn't exist
        if not node:
            return None
        nodeMap = {}
        self.dfs(node,nodeMap)
        return nodeMap[node]


    def dfs(self,node, nodeMap):
        if node not in nodeMap:
            nodeMap[node] = Node(node.val)
            nodeMap[node].neighbors = []
        for neighborNode in node.neighbors:
            # If NeighborNode has not been created, create it
            if neighborNode not in nodeMap:
                self.dfs(neighborNode,nodeMap)
            nodeMap[node].neighbors.append(nodeMap[neighborNode])




        

