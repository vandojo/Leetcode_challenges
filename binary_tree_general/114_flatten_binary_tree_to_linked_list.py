'''description

Given the root of a binary tree, flatten the tree into a "linked list":

    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''

# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        currNode = root

        while currNode:
            if currNode.left is not None:
                lastNode = currNode.left
                
                while lastNode.right is not None:
                    lastNode = lastNode.right
                
                lastNode.right = currNode.right
                currNode.right = currNode.left
                currNode.left = None

            currNode = currNode.right