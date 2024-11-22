'''Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.'''


# Solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def order(self, node: Optional[TreeNode], vals: List[int]):

        if node is None:
            return

        self.order(node.left, vals)
        vals.append(node.val)
        self.order(node.right, vals)
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return

        

        vals = []
        self.order(root, vals)

        res = float('inf')
        for i in range(1, len(vals)):
            res = min(res, vals[i] - vals[i-1])
        
        return res