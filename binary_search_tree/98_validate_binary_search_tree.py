'''Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left
    subtree
    of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
'''


# Solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkBST(self, node, min_val, max_val):
        if not node:
            return True
        if (min_val is not None and node.val <= min_val) or (max_val is not None and node.val >= max_val):
            return False
        return self.checkBST(node.left, min_val, node.val) and self.checkBST(node.right, node.val, max_val)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, float('-inf'), float('inf'))
        