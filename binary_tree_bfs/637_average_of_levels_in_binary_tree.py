'''Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted. '''


# SOLUTION

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        que = deque([root])
        res = []

        while que:
            level = len(que)
            amt = 0

            for i in range(level):
                node = que.popleft()
                amt += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            avg = amt / level
            res.append(avg)

        

        return res