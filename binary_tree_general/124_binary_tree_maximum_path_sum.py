'''description

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

'''

# Solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = float(-inf)

        def maxSum(node):

            if node == None:
                return 0
            nonlocal ans
            left = maxSum(node.left)
            right = maxSum(node.right)

            left = max(left, 0)
            right = max(right,0)

            ans = max(ans, node.val + left + right)

            return node.val + max(left, right)
        
        maxSum(root)
        return ans

