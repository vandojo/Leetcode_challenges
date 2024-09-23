'''description

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.'''


# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def rootLeaf(node, val):

            if node == None:
                return 0
            
            val = (val * 10) + node.val

            if not node.left and not node.right:
                return val
            
            return rootLeaf(node.left, val) + rootLeaf(node.right, val)
        
        return rootLeaf(root, 0)