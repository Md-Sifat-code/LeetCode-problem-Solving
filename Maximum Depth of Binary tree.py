# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_part = self.maxDepth(root.left)
        right_part = self.maxDepth(root.right)

        return 1 + max(left_part, right_part)
        