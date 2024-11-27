'''Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree'''


# SOLUTION

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        node = root
        vals = []
        amt = 0

        while node or vals:
            while node:
                vals.append(node)
                node = node.left
            node = vals.pop()
            amt += 1
            if amt == k:
                return node.val
            node = node.right



        