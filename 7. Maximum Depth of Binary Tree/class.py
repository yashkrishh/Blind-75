# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 # Base case: if node is null, return 0

        left_height = self.maxDepth(root.left)   # Get height of left subtree
        right_height = self.maxDepth(root.right) # Get height of right subtree

        return 1 + max(left_height, right_height) # Height of current node
        
