# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # For this problem, we should do level traversal 

        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            level = []
            queueLen = len(queue)

            for _ in range(queueLen):
                curNode = queue.popleft()

                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                level.append(curNode.val)
            res.append(level)
        return res
        




