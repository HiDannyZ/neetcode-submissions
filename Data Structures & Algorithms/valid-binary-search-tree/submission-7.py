# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.checkBST(root,float("-inf"), float("inf"))
    
    def checkBST(self, root, lowerBound, upperBound):

        if not root:
            return True
        
        if root.val <= lowerBound or root.val >= upperBound:
            return False

        return self.checkBST(root.left, lowerBound, root.val) and self.checkBST(root.right,root.val, upperBound )
        