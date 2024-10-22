'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

'''



# Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, left_tree, right_tree, hash_map, postorder):

        if left_tree > right_tree:
            return None

        # root is last value of postorder
        root = TreeNode(postorder.pop())

        idx = hash_map[root.val]

        root.right = self.helper(idx+1, right_tree, hash_map, postorder)
        root.left = self.helper(left_tree, idx-1, hash_map, postorder)

        return root
        




    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        hash_map = {val : idx for idx, val in enumerate(inorder)}
        return self.helper(0, len(inorder)-1, hash_map, postorder)

        